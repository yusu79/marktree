import sys
import pyperclip

from .core import render_tree
from .exceptions import (
    InputFileNotFoundError,
    InvalidEncodingError,
    InvalidInputError,
    InvalidMarkdownError,
)
from .usage import usage_en, usage_jp

# パイプやリダイレクト時も UTF-8 で出力する
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

def print_error(title: str, message: str) -> None:
    print(
        f"\033[91m"
        f"Error: {title}\n"
        f"{message}"
        f"\033[0m",
        file=sys.stderr,
    )

def main():
    """
    CLIエントリーポイント。
    コマンドライン引数を解析し、処理を実行する。

    - -h/--help         → 英語ヘルプを表示して終了
    - --help_jp         → 日本語ヘルプを表示して終了
    - -C/-c/--clip      → クリップボードから入力を取得
    - --copy            → 結果をクリップボードへコピー
    - -L/-l/--level     → 出力する最大見出しレベルを指定（1～6）
    - -P/-p/--plain     → プレーン出力に切り替え
    - -E/-e/--encoding  → ファイルエンコーディングを指定
    - ファイルパス      → 指定されたMarkdownファイルを処理
    """

    # デフォルト値
    options = dict(
        filename=None,
        lines=None,
        print_depth=6,
        plain=False,
        encoding="utf-8",
        copy=False,
    )

    i = 1

    try:
        while i < len(sys.argv):
            arg = sys.argv[i]

            if arg in ["-h", "--help"]:
                usage_en()
                return 0

            elif arg in ["--help-jp", "--help_jp"]:
                usage_jp()
                return 0

            elif arg in ["-C", "-c", "--clip"]:
                try:
                    clipboard = pyperclip.paste()
                    options["lines"] = clipboard.split("\r\n") if clipboard else []
                except Exception as e:
                    print_error(
                        "Clipboard Read Failed",
                        f"クリップボードの読み取りに失敗しました: {e}",
                    )
                    return 1
                i += 1

            elif arg == "--copy":
                options["copy"] = True
                i += 1

            elif arg in ["-L", "-l", "--level"]:
                try:
                    options["print_depth"] = int(sys.argv[i + 1])
                except IndexError:
                    print_error(
                        "Missing Hierarchy Level",
                        "階層レベルを指定してください。例: -L 2",
                    )
                    return 1
                except ValueError:
                    print_error(
                        "Invalid Hierarchy Level",
                        "階層には正の整数を指定してください。例: -L 2",
                    )
                    return 1
                i += 2

            elif arg in ["-P", "-p", "--plain"]:
                options["plain"] = True
                i += 1

            elif arg in ["-E", "-e", "--encoding"]:
                try:
                    options["encoding"] = sys.argv[i + 1]
                except IndexError:
                    print_error(
                        "Missing Encoding",
                        "文字コードを指定してください。例: -E utf-8",
                    )
                    return 1
                i += 2

            elif arg.startswith("-"):
                print_error(
                    "Invalid Option",
                    "無効なオプションです。--help を使用してください。",
                )
                return 1

            else:
                options["filename"] = arg
                i += 1

    except Exception as e:
        print_error(
            "Error: Unexpected Error",
            f"予期せぬエラーが発生しました: {e}"
        )
        return 1

    # 階層レベルチェック
    depth = options["print_depth"]
    if not 1 <= depth <= 6:
        print_error(
            "Error: Hierarchy Level Out of Range",
            "階層は1から6までの間で指定してください。"
        )
        return 1

    copy = options.pop("copy")

    try:
        text = render_tree(**options)

    except InputFileNotFoundError:
        print_error(
            "File Not Found",
            "指定されたMarkdownファイルが見つかりません。",
        )
        return 1

    except InvalidEncodingError:
        print_error(
            "Unknown Encoding",
            "指定された文字コードはサポートされていません。\n"
            "utf-8, cp932, shift_jis などを指定してください。",
        )
        return 1

    except InvalidInputError:
        print_error(
            "Invalid Input",
            "入力ファイルまたは入力テキストを指定してください。",
        )
        return 1

    except InvalidMarkdownError:
        print_error(
            "Empty Heading",
            "Markdownファイルから文章のない見出し（#）が検出されました。",
        )
        return 1

    if copy:
        pyperclip.copy(text)
    else:
        print(text, end="")

    return 0
