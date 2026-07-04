class MarktreeError(Exception):
    """marktree の基底例外。"""


class InputFileNotFoundError(MarktreeError):
    """入力ファイルが見つからなかった。"""


class InvalidEncodingError(MarktreeError):
    """文字コードが不正、またはデコードに失敗した。"""


class InvalidInputError(MarktreeError):
    """入力が不正。"""


class InvalidMarkdownError(MarktreeError):
    """Markdown の解析に失敗した。"""
