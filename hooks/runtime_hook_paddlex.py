# PyInstaller runtime hook for paddlex
# This hook MUST run BEFORE paddlex is imported anywhere
#
# Strategy:
# 1. Use a PEP 451-compliant import hook to intercept paddlex.utils.deps and patch it after loading
# 2. Create the .version file for paddlex
# 3. Set environment variables to signal we're in a bundled app
#
# IMPORTANT: We must NOT inject fake parent modules (paddlex, paddlex.utils)
# as this would prevent the real modules from loading!

import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import os
import sys


def setup_import_hook():
    """
    Set up a PEP 451-compliant import hook that patches paddlex.utils.deps when it's loaded.
    This allows the real paddlex package to load normally, but patches
    the dependency checker to skip runtime checks.
    """
    if not hasattr(sys, '_MEIPASS'):
        return  # Only needed in PyInstaller bundle

    class PaddlexDepsLoader(importlib.abc.Loader):
        """PEP 451 loader that loads paddlex.utils.deps and then patches it."""

        def __init__(self, original_spec):
            self._original_spec = original_spec

        def create_module(self, spec):
            # Use default semantics (return None to get a new module object)
            return None

        def exec_module(self, module):
            # Execute the real module using its original loader
            self._original_spec.loader.exec_module(module)
            # Now patch the loaded module
            _patch_deps_module(module)
            print(f"Runtime hook: Patched {module.__name__}")

    class PaddlexDepsFinder(importlib.abc.MetaPathFinder):
        """
        PEP 451-compliant meta path finder that intercepts paddlex.utils.deps
        and wraps it with a patching loader.
        """
        _patched = False

        def find_spec(self, fullname, path, target=None):
            if fullname != 'paddlex.utils.deps' or self._patched:
                return None

            # Temporarily remove ourselves to avoid recursion
            sys.meta_path.remove(self)
            try:
                original_spec = importlib.util.find_spec(fullname)
            except (ModuleNotFoundError, ValueError):
                original_spec = None
            finally:
                sys.meta_path.insert(0, self)

            if original_spec is None or original_spec.loader is None:
                # Return a spec backed by a stub loader
                stub_loader = _StubDepsLoader()
                return importlib.machinery.ModuleSpec(fullname, stub_loader)

            self._patched = True
            return importlib.machinery.ModuleSpec(
                fullname,
                PaddlexDepsLoader(original_spec),
                origin=original_spec.origin,
            )

    class _StubDepsLoader(importlib.abc.Loader):
        """Fallback loader that creates a minimal stub for paddlex.utils.deps."""

        def create_module(self, spec):
            return None

        def exec_module(self, module):
            _populate_stub_deps_module(module)
            print(f"Runtime hook: Created stub for {module.__name__}")

    # Install the finder at the front of meta_path
    sys.meta_path.insert(0, PaddlexDepsFinder())
    print("Runtime hook: Installed paddlex.utils.deps import hook (PEP 451)")


def _patch_deps_module(module):
    """Patch a loaded paddlex.utils.deps module so all dependency checks are no-ops."""
    module.require_extra = lambda *a, **kw: None

    if hasattr(module, 'check_deps'):
        module.check_deps = lambda *a, **kw: None
    if hasattr(module, 'is_dep_available'):
        module.is_dep_available = lambda *a, **kw: True
    if hasattr(module, 'ensure_deps'):
        module.ensure_deps = lambda *a, **kw: None

    # Patch _wrapper if it exists (it is a decorator that calls require_extra)
    if hasattr(module, '_wrapper'):
        original_wrapper = module._wrapper

        def patched_wrapper(*args, **kwargs):
            """Patched wrapper that silently ignores DependencyError."""
            try:
                return original_wrapper(*args, **kwargs)
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                if 'DependencyError' in error_type or 'requires additional dependencies' in error_msg:
                    return None
                raise

        module._wrapper = patched_wrapper
        print("Runtime hook: Patched _wrapper function")


def _populate_stub_deps_module(module):
    """Populate a fresh module object as a minimal paddlex.utils.deps stub."""
    module.require_extra = lambda *a, **kw: None
    module.check_deps = lambda *a, **kw: None
    module.is_dep_available = lambda *a, **kw: True
    module.ensure_deps = lambda *a, **kw: None
    module.get_extra_deps = lambda *a, **kw: {}

    class DependencyError(Exception):
        pass

    module.DependencyError = DependencyError


def ensure_paddlex_version():
    """Create the paddlex .version file if it doesn't exist."""
    PADDLEX_VERSION = '3.3.10'  # Updated by CI build script

    if not hasattr(sys, '_MEIPASS'):
        return  # Not needed when running normally

    base_path = sys._MEIPASS
    paddlex_dir = os.path.join(base_path, 'paddlex')
    version_file = os.path.join(paddlex_dir, '.version')

    # Create directory if it doesn't exist
    try:
        os.makedirs(paddlex_dir, exist_ok=True)
    except Exception as e:
        print(f"Warning: Could not create paddlex directory: {e}")
        return

    # Create .version file if it doesn't exist
    if not os.path.exists(version_file):
        try:
            with open(version_file, 'w', encoding='utf-8') as f:
                f.write(PADDLEX_VERSION)
            print(f"Runtime hook: Created {version_file} with version {PADDLEX_VERSION}")
        except Exception as e:
            print(f"Warning: Could not create .version file: {e}")


def set_environment_flags():
    """Set environment variables to signal we're in a bundled app."""
    if hasattr(sys, '_MEIPASS'):
        os.environ['PADDLEX_SKIP_DEPS_CHECK'] = '1'
        os.environ['PADDLEX_BUNDLED'] = '1'
        os.environ['PYINSTALLER_BUNDLED'] = '1'


# Run all setup functions immediately when this hook is loaded.
# Order matters!
set_environment_flags()
setup_import_hook()
ensure_paddlex_version()

print("Runtime hook: PaddleX setup complete")
