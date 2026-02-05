from setuptools import setup, find_packages

setup(
    name="enes193",  # Package name
    version="1.0.0", 
    license= 'MIT', 
    description="A MicroPython library for ESP32-based ENES193 course project.",
    author="Keystone Center", 
    url="https://github.com/umdenes100/enes193",
    packages=['enes193'], 
    classifiers=[
        "Intended Audience :: UMD Students",
        "Programming Language :: MicroPython :: 1.24",
        "Topic :: Communications",
    ],
    keywords="MicroPython ESP32 WebSocket ENES193",
)