# Python + Rust — 10 Code Examples

This ZIP contains 10 Python examples plus a small Rust/PyO3 extension demo.

## Run Python
python 01_hello_world.py

## Build the Rust extension
cd rust_demo
pip install maturin
maturin develop
cd ..
python 10_python_rust_bridge.py
