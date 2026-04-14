"""Compile uau_api to Cython native extensions (.so / .pyd).

Prerequisites (one-time setup):
    sudo apt-get install -y gcc python3-dev    # Debian / Ubuntu / WSL
    # macOS: xcode-select --install
    # Windows: install Visual C++ Build Tools

Build:
    uv run python compile.py build_ext --inplace

Post-build — strip Python sources, keep only __init__.py stubs:
    find uau_api -name "*.py" ! -name "__init__.py" -delete
    find uau_api -name "*.c" -delete

The result is a package tree containing only native extensions (.so) and
minimal __init__.py stubs — the original Python source is no longer present.
"""
from setuptools import setup
from Cython.Build import cythonize
import glob

# Exclude __init__.py files — they must remain as plain Python so Python
# recognises the directories as packages when importing compiled extensions.
sources = [
    f for f in glob.glob("uau_api/**/*.py", recursive=True)
    if not f.endswith("__init__.py")
]

setup(
    name="uau-api",
    ext_modules=cythonize(
        sources,
        compiler_directives={"language_level": "3"},
        nthreads=4,
    ),
)
