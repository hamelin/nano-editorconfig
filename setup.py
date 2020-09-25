from setuptools import setup, find_packages


setup(
    name="nano-editorconfig",
    version="1.0",
    packages=find_packages(),
    scripts=["nec"],
    author="Benoit Hamelin",
    author_email="benoit@benoithamelin.com",
    description="Wrapper around GNU nano to enable EditorConfig features",
    license="MIT",
    install_requires=["editorconfig"],
    url="https://github.com/hamelin/nano-editorconfig",
    python_requires=">=3.6"
)
