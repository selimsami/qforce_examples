"""
Qforce Examples
Example and test files for Qforce.
"""
import sys
from setuptools import setup, find_packages

short_description = "Example and test files for Qforce.".split("\n")[0]

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = None


setup(
    # Self-descriptive entries which should always be present
    name='qforce_examples',
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Which Python importable modules should be included when your package is installed
    # Handled automatically by setuptools. Use 'exclude' to prevent some specific
    # subpackage(s) from being added, if needed
    packages=find_packages(),

    # Optional include package data to ship with your package
    # Customize MANIFEST.in if the general case does not suit your needs
    # Comment out this line to prevent the files from being packaged with your software
    include_package_data=True,
)
