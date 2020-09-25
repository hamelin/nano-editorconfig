import pathlib as pl
from typing import *

import editorconfig as ec


def iter_rc_file(path_to_edit: Optional[pl.Path], paths_rc_base: List[pl.Path]) -> Iterator[str]:
    config_ec = {}
    if path_to_edit:
        config_ec = ec.get_properties(path_to_edit.expanduser().resolve())
    yield from iter_rc_file_from_config(paths_rc_base, config_ec)


def iter_rc_file_from_config(paths_rc_base: List[pl.Path], config_ec: Dict[str, str]) -> Iterator[str]:
    for path_base in paths_rc_base:
        p = path_base.expanduser()
        if p.is_file():
            yield p.read_text()

    if "insert_final_newline" in config_ec:
        yield f"{dict(true='un', false='')[config_ec['insert_final_newline']]}set nonewlines"
    if "indent_size" in config_ec or "tab_width" in config_ec:
        yield f"set tabsize {config_ec.get('indent_size') or config_ec.get('tab_width', '8')}"
    if "indent_style" in config_ec:
        yield f"{dict(tab='un', space='')[config_ec['indent_style']]}set tabstospaces"
    if "max_line_length" in config_ec:
        yield f"set fill {config_ec['max_line_length']}"
