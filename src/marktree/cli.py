import sys, pyperclip
from .core import print_tree
from .usage import usage_en, usage_jp

def main():
    """
    CLIエントリーポイント。
    コマンドライン引数を解析し、処理を実行する。

    - -h/--help         → 英語ヘルプを表示して終了
    - --help_jp         → 日本語ヘルプを表示して終了
    - -C/-c/--clip      → クリップボードから入力を取得
    - -L/-l/--level     → 出力する最大見出しレベルを指定（1～6）
    - -P/-p/--plane     → プレーン出力に切り替え
    - -E/-e/--encoding  → ファイルエンコーディングを指定（例: utf-8, cp932）
    - ファイルパス      → 指定されたMarkdownファイルを処理
    """
    # デフォルト値
    options = dict(
        filename=None,
        lines=None,
        print_depth=6,
        plane=False,
        encoding="utf-8",   # 追加: デフォルトはUTF-8
    )

    i = 1
    try:
        while i < len(sys.argv):
            arg = sys.argv[i]

            if arg in ["-h", "--help"]:
                usage_en()
                sys.exit(0)

            elif arg in ["--help-jp", "--help_jp"]:
                usage_jp()
                sys.exit(0)

            elif arg in ["-C", "-c", "--clip"]:
                try:
                    clipboard = pyperclip.paste()
                    if clipboard:
                        options['lines'] = clipboard.split("\r\n")
                    else:
                        options['lines'] = []
                except Exception as e:
                    print(f"\033[91mError: Clipboard Read Failed\nクリップボードの読み取りに失敗しました: {e}\033[0m")
                    sys.exit(1)
                i += 1

            elif arg in ["-L", "-l", "--level"]:
                try:
                    value = sys.argv[i + 1]
                except IndexError:
                    print("\033[91mError: Missing Hierarchy Level\n階層レベルを指定してください。例: -L 2\033[0m")
                    sys.exit(1)
                try:
                    options['print_depth'] = int(value)
                except ValueError:
                    print("\033[91mError: Invalid Hierarchy Level\n階層には正の整数を指定してください。例: -L 2\033[0m")
                    sys.exit(1)
                i += 2

            elif arg in ["-P", "-p", "--plane"]:
                options['plane'] = True
                i += 1

            elif arg in ["-E", "-e", "--encoding"]:
                try:
                    options['encoding'] = sys.argv[i + 1]
                except IndexError:
                    print("\033[91mError: Missing Encoding\n文字コードを指定してください。例: -E cp932\033[0m")
                    sys.exit(1)
                i += 2

            elif arg.startswith("-"):
                print("\033[91mError: Invalid Option\n無効なオプションです。--help を使用してください。\033[0m")
                sys.exit(1)

            else:
                options['filename'] = arg
                i += 1

    except Exception as e:
        print(f"\033[91mError: Unexpected Error\n予期せぬエラーが発生しました: {e}\033[0m")
        sys.exit(1)

    # 階層レベルチェック
    depth = options.get('print_depth')
    if depth is None or not 1 <= depth <= 6:
        print("\033[91mError: Hierarchy Level Out of Range\n階層は1から6までの間で指定してください。\033[0m")
        sys.exit(1)

    # 関数呼び出し
    return print_tree(**options)
