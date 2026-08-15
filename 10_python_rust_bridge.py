# Concept demo: call Rust from Python using PyO3.
# Install maturin first: pip install maturin
# This file only shows the Python side.

try:
    import rust_math
    print("Rust says:", rust_math.add(10, 20))
except ImportError:
    print("Build the Rust extension first using maturin.")