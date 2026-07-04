# =========================
# 多言語メッセージ定義
# =========================

MESSAGES = {
    "en": {
        "clipboard_read_failed": (
            "Clipboard Read Failed",
            "Failed to read clipboard: {error}",
        ),
        "missing_level": (
            "Missing Hierarchy Level",
            "Please specify hierarchy level. e.g. -L 2",
        ),
        "invalid_level": (
            "Invalid Hierarchy Level",
            "Hierarchy level must be a positive integer. e.g. -L 2",
        ),
        "missing_encoding": (
            "Missing Encoding",
            "Please specify encoding. e.g. -E utf-8",
        ),
        "invalid_option": (
            "Invalid Option",
            "Invalid option. Use --help.",
        ),
        "unexpected_error": (
            "Unexpected Error",
            "An unexpected error occurred: {error}",
        ),
        "level_out_of_range": (
            "Hierarchy Level Out of Range",
            "Hierarchy level must be between 1 and 6.",
        ),
        "file_not_found": (
            "File Not Found",
            "Specified markdown file was not found.",
        ),
        "invalid_encoding": (
            "Unknown Encoding",
            "Unsupported encoding. Use utf-8, cp932, shift_jis, etc.",
        ),
        "invalid_input": (
            "Invalid Input",
            "No input file.",
        ),
        "empty_heading": (
            "Empty Heading",
            "Markdown contains empty headings (# only lines are not allowed).",
        ),
    },
    "ja": {
        "clipboard_read_failed": (
            "クリップボード読み取り失敗",
            "クリップボードの読み取りに失敗しました: {error}",
        ),
        "missing_level": (
            "階層レベル未指定",
            "階層レベルを指定してください。例: -L 2",
        ),
        "invalid_level": (
            "無効な階層レベル",
            "階層レベルは正の整数で指定してください。例: -L 2",
        ),
        "missing_encoding": (
            "文字コード未指定",
            "文字コードを指定してください。例: -E utf-8",
        ),
        "invalid_option": (
            "無効なオプション",
            "--help を使用してください。",
        ),
        "unexpected_error": (
            "予期せぬエラー",
            "予期せぬエラーが発生しました: {error}",
        ),
        "level_out_of_range": (
            "階層レベル範囲エラー",
            "階層は1から6の間で指定してください。",
        ),
        "file_not_found": (
            "ファイル未検出",
            "指定されたMarkdownファイルが見つかりません。",
        ),
        "invalid_encoding": (
            "未対応の文字コード",
            "utf-8, cp932, shift_jis などを指定してください。",
        ),
        "invalid_input": (
            "入力エラー",
            "入力ファイルを指定してください。",
        ),
        "empty_heading": (
            "空の見出し検出",
            "見出しの内容がありません（# の後にテキストが必要です）",
        ),
    },
}

def get_message(lang: str, key: str, **kwargs):
    title, text = MESSAGES.get(lang, MESSAGES["en"])[key]
    return title, text.format(**kwargs)
