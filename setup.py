import setuptools
import superlevure

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="superlevure",
    version=superlevure.__version__,
    author="superlevure",
    author_email="superlevure.dev@gmail.com",
    description="Superlevure library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/superlevure/superlevure",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)

