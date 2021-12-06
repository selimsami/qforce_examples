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

    packages=['qforce_examples'],
    package_dir={'qforce_examples': 'src'},
    package_data={'qforce_examples': ['../examples']},

    # Optional include package data to ship with your package
    # Customize MANIFEST.in if the general case does not suit your needs
    # Comment out this line to prevent the files from being packaged with your software
    include_package_data=True,

    # Allows `setup.py test` to work correctly with pytest
    # setup_requires=[] + pytest_runner,

    # Additional entries you may want simply uncomment the lines you want and fill in the data
    # url='http://www.my_package.com',  # Website
    # install_requires=[],              # Required packages, pulls from pip if needed; do not use for Conda deployment
    # platforms=['Linux',
    #            'Mac OS-X',
    #            'Unix',
    #            'Windows'],            # Valid platforms your code works on, adjust to your flavor
    # python_requires=">=3.5",          # Python version restrictions

    # Manual control if final package is compressible or not, set False to prevent the .egg from being made
    # zip_safe=False,

)
