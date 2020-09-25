# nano-editorconfig, the `nec` plus ultra

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
