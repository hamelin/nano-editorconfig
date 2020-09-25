from setuptools import setup, find_packages


long_description="""\
The [GNU Nano](https://nano-editor.org/) editor does not provide any support for
[EditorConfig](https://editorconfig.org/) generalized configuration. This package offers a wrapper named `nec` that
generates a Nano configuration file on-the-fly, based on EditorConfig settings applicable to the first editable
file named on the command line.

Remark that many EditorConfig settings are not supported by Nano. For instance, Nano does not handle any other
text encoding besides UTF-8 (or even ASCII, if UTF-8 support is not built in). The EditorConfig settings that are
handled by this package are:

- `indent_style`
- `indent_size`
- `tab_width` (overriden by `indent_size`)
- `insert_final_newline`
- `max_line_length`
"""


setup(
    name="nano-editorconfig",
    version="1.0",
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
