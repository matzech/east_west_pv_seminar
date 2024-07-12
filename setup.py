from setuptools import setup, find_packages

setup(
    python_requires=">=3.6",
    install_requires=[
        "xarray",
        "atlite",
        "jupyter",
        "cartopy",
        "demandlib",# used for the demand calculations
        "matplotlib",
        "cartopy"
    ],
)