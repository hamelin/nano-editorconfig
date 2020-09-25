from setuptools import setup, find_packages


DESC = """\
TBD
"""

setup(
    name="nano-editorconfig",
    version="0.0.1",
    packages=find_packages(),
    scripts=["nec"],
    author="Benoit Hamelin",
    author_email="benoit@benoithamelin.com",
    description="Wrapper around GNU nano to enable EditorConfig features",
    long_description=DESC,
    license="MIT",
    install_requires=["editorconfig"],
    url="https://github.com/hamelin/nano-editorconfig",
    python_requires=">=3.6"
)
