import sys, pyperclip
from .core import render_tree
from .usage import usage_en, usage_jp

# パイプやリダイレクト時も UTF-8 で出力する
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


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
                    options["lines"] = clipboard.splitlines() if clipboard else []
                    if clipboard:
                        options['lines'] = clipboard.split("\r\n")
                    else:
                        options['lines'] = []
                except Exception as e:
                    print(
                        f"\033[91mError: Clipboard Read Failed\n"
                        f"クリップボードの読み取りに失敗しました: {e}\033[0m"
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
                    print("\033[91mError: Missing Hierarchy Level\n階層レベルを指定してください。例: -L 2\033[0m")
                    return 1
                except ValueError:
                    print("\033[91mError: Invalid Hierarchy Level\n階層には正の整数を指定してください。例: -L 2\033[0m")
                    return 1
                i += 2

            elif arg in ["-P", "-p", "--plain"]:
                options['plain'] = True
                i += 1

            elif arg in ["-E", "-e", "--encoding"]:
                try:
                    options['encoding'] = sys.argv[i + 1]
                except IndexError:
                    print("\033[91mError: Missing Encoding\n文字コードを指定してください。例: -E utf-8\033[0m")
                    return 1
                i += 2

            elif arg.startswith("-"):
                print("\033[91mError: Invalid Option\n無効なオプションです。--help を使用してください。\033[0m")
                return 1

            else:
                options['filename'] = arg
                i += 1

    except Exception as e:
        print(f"\033[91mError: Unexpected Error\n予期せぬエラーが発生しました: {e}\033[0m")
        return 1

    # 階層レベルチェック
    depth = options["print_depth"]
    if not 1 <= depth <= 6:
        print("\033[91mError: Hierarchy Level Out of Range\n階層は1から6までの間で指定してください。\033[0m")
        return 1

    copy = options.pop("copy")

    text = render_tree(**options)

    if copy:
        pyperclip.copy(text)
    else:
        print(text, end="")

    return 0
