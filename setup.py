from setuptools import setup, find_packages

setup(
    name="3d_reconstruction_from_2d_images",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)