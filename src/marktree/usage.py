def usage_en():
    print("""
usage: marktree [options] [foo.md]

Convert headings in a Markdown file (.md) into a tree-like structure and output.

positional arguments:
  file                 Pass the Markdown file for which you want to output headings in a tree.

optional arguments:
  -h, --help           Display help in English
  --help-jp            Display help in Japanese
  -L, -l, --level LEVEL
                       Display headings up to the specified level (default: 6)
  -C, -c, --clip       Read from the clipboard and convert the copied Markdown text into a tree structure
  -P, -p, --plane      Output only the raw headings without tree formatting
  -E, -e, --encoding ENCODING
                       Specify file encoding (default: utf-8, e.g., cp932)
""")


def usage_jp():
    print("""
使い方: marktree [オプション] [foo.md]

Markdown ファイル (.md) の見出しを木構造に変換して出力します。

引数:
    foo.md             見出しを木構造として出力したい Markdown ファイルを指定

オプション:
    -h, --help         ヘルプを表示
    --help-jp          ヘルプを日本語で表示
    -L, -l, --level    表示する見出しレベルを指定 (デフォルト: 6)
    -C, -c, --clip     クリップボードから Markdown テキストを読み取り木構造に変換
    -P, -p, --plane    見出しをツリー整形せずそのまま出力
    -E, -e, --encoding ファイルのエンコーディングを指定 (デフォルト: utf-8, 例: cp932)
""")
