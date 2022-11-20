import setuptools
from pathlib import Path

setuptools.setup(
    name="sample_package",
    version=1.0,
    long_description=Path("README.md").read_text(),
    # .find_packages() will automatically look for all packages in our directory
    packages=setuptools.find_packages(exclude=["test", "data"])
)
