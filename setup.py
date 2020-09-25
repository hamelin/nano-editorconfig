from setuptools import setup, find_packages


with open("README.md", "rt") as file:
    long_description=file.read()


setup(
    name="nano-editorconfig",
    version="1.0.1",
    packages=find_packages(),
    scripts=["nec"],
    author="Benoit Hamelin",
    author_email="benoit@benoithamelin.com",
    description="Wrapper around GNU nano to enable EditorConfig features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=["editorconfig"],
    url="https://github.com/hamelin/nano-editorconfig",
    python_requires=">=3.6"
)
