USAGE = {
    "en": """usage: marktree [options] [foo.md]

Convert headings in a Markdown file (.md) into a tree-like structure and output.

positional arguments:
  file                 Pass the Markdown file for which you want to output headings in a tree.

optional arguments:
  -h, --help                    Display help
  -L, --level [LEVEL]           Display headings up to the specified level (default: 6)
  -C, --clip                    Read from the clipboard
  -P, --plane                   Output only the raw headings without tree formatting
  -E, --encoding [ENCODING]     Specify file encoding (default: utf-8, e.g., cp932)
  --copy                        Copy result to clipboard
""",

    "ja": """使い方: marktree [オプション] [hoge.md]

Markdownファイル (.md) の見出しを木構造に変換して出力します。

引数:
  hoge.md            木構造に変換するMarkdownファイルを指定

オプション:
  -h, --help                           ヘルプを表示
  -L, --level [階層]                   表示する見出しレベルを指定 (デフォルト: 6)
  -C, --clip                           クリップボードを読み込む
  -P, --plane                          見出しをツリー整形せずそのまま出力
  -E, --encoding [エンコーディング]    ファイルのエンコーディングを指定 (デフォルト: utf-8, 例: cp932)
  --copy                               結果をクリップボードにコピー
""",
}

def print_usage(lang: str):
    print(USAGE.get(lang, USAGE["en"]))
