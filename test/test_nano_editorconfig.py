from unittest.mock import MagicMock

from nano_editorconfig import iter_rc_file_from_config


def test_no_path_base():
    assert [] == list(iter_rc_file_from_config([], {}))


def mock_path(text):
    p = MagicMock()
    p.expanduser.return_value = p
    p.is_file.return_value = True
    p.read_text.return_value = text
    return p


def test_few_paths_base():
    p1 = mock_path("asdf\nqwer")
    p2 = mock_path("heyhey")
    p3 = mock_path("1\n2\n3")
    assert ["asdf\nqwer", "heyhey", "1\n2\n3"] == list(iter_rc_file_from_config([p1, p2, p3], {}))


def test_path_not_a_file():
    p = mock_path("not gonna see this")
    p.is_file.return_value = False
    assert [] == list(iter_rc_file_from_config([p], {}))


def test_final_newline_true():
    assert ["unset nonewlines"] == list(iter_rc_file_from_config([], {"insert_final_newline": "true"}))


def test_final_newline_false():
    assert ["set nonewlines"] == list(iter_rc_file_from_config([], {"insert_final_newline": "false"}))


def test_indent_size():
    assert ["set tabsize 4"] == list(iter_rc_file_from_config([], {"indent_size": 4}))


def test_indent_size_from_tab_width():
    assert ["set tabsize 2"] == list(iter_rc_file_from_config([], {"tab_width": 2}))


def test_indent_size_precedence():
    assert ["set tabsize 4"] == list(iter_rc_file_from_config([], {"tab_width": 8, "indent_size": 4}))


def test_indent_style_tab():
    assert ["unset tabstospaces"] == list(iter_rc_file_from_config([], {"indent_style": "tab"}))


def test_ident_style_space():
    assert ["set tabstospaces"] == list(iter_rc_file_from_config([], {"indent_style": "space"}))


def test_max_line_length():
    assert ["set fill 118"] == list(iter_rc_file_from_config([], {"max_line_length": 118}))


def test_all_together():
    assert [
        "abcd",
        "heyhey\nhoho",
        "unset nonewlines",
        "set tabsize 2",
        "unset tabstospaces",
        "set fill 78"
    ] == list(iter_rc_file_from_config(
        [mock_path("abcd"), mock_path("heyhey\nhoho")],
        {
            "end_of_line": "lf",
            "insert_final_newline": "true",
            "charset": "utf-8",
            "indent_size": "2",
            "indent_style": "tab",
            "trim_trailing_whitespace": "true",
            "max_line_length": "78",
            "tab_width": "8"
        }
    ))
