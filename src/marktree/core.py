import sys

def append_tree_branch(depth, name, dict, output):
    """
    ツリーの1行を生成して output に追加する。

    Args:
        depth (int): 見出しレベル（# の数）
        name (str): 見出しの名前
        dict (dict): 各レベルに「見出しが存在するかどうか」を記録する辞書
        output (list): 出力用の文字列リスト
    """
    mozi = ""
    for i in range(1, 7):
        if i < depth:
            if dict[i] == "exist":
                mozi += "│  "
            else:
                mozi += "   "
        elif i == depth:
            if dict[i] == "exist":
                mozi += f"├── {name}"
            else:
                mozi += f"└── {name}"
            dict[i] = "exist"
        else:
            dict[i] = "none"
    output.append(mozi)


def generate_tree_view(lines, print_depth):
    """
    Markdownテキストを解析し、ツリー形式で見出しを表示する。

    - コードブロック内の見出し (#) は無視する
    - 指定された深さ (print_depth) まで表示する

    Args:
        lines (list[str]): 入力テキスト行
        print_depth (int): 出力する最大見出しレベル
    """

    current_depth = 0
    current_name = ""
    dict = {i: "none" for i in range(1, 7)}
    output = []
    ignore_code_block = False
    for line in reversed(lines):
        if line.startswith("```"):
            ignore_code_block = not ignore_code_block
        if ignore_code_block:
            continue
        else:
            if line.startswith('#'):
                current = line.split(None, 1)
                current_depth = len(current[0])
                current_name = current[1].strip("\n")
                if current_depth <= print_depth:
                    append_tree_branch(current_depth, current_name, dict, output)

    for i in reversed(output):
        print(i)
    print("")


def generate_plain_view(lines, print_depth):
    """
    見出しをツリー化せず、そのまま出力する。

    - コードブロック内は無視
    - 指定された深さ (print_depth) まで出力
    """
    ignore_code_block = False
    for line in lines:
        if line.startswith("```"):
            ignore_code_block = not ignore_code_block
        if ignore_code_block:
            continue
        else:
            if line.startswith("#"):
                current = line.split(None, 1)
                depth = len(current[0])
                if depth <= print_depth:
                    print(line.strip("\n"))
    print("")

def print_tree(filename=None, lines=None, print_depth=6, plane=False, encoding="utf-8"):
    """
    ファイルまたは入力テキストから見出しを読み取り、ツリーまたは平文で表示する。

    Args:
        filename (str|None): Markdownファイルパス（Noneなら lines を使う）
        lines (list[str]|None): 入力テキスト
        print_depth (int): 出力する最大見出しレベル
        plane (bool): Trueならプレーン出力、Falseならツリー出力
        encoding (str): ファイルの文字コード（デフォルトは utf-8）

    Raises:
        LookupError: サポートされていないも文字コードを指定した場合
        UnicodeDecodeError: デコードできない場合
        FileNotFoundError: ファイルが存在しない場合
        IndexError: 空見出し (# だけ) が存在する場合
    """
    try:
        if filename is not None:
            try: 
                with open(filename, 'r', encoding=encoding) as file:
                    lines = file.readlines()
            except LookupError:
                print(f"\033[91mError: Unknown Encoding\n指定された文字コード '{encoding}' はサポートされていません。正しいエンコーディング名を指定してください（例: utf-8, cp932, shift_jis）。\033[0m")
                sys.exit(1)
            except UnicodeDecodeError as e:
                print(f"\033[91mError: Decode Failed\nファイルを '{encoding}' でデコードできませんでした。"
                    f"ファイルの実際の文字コードと一致しているか確認してください。\n詳細: {e}\033[0m")
                sys.exit(1)

        if plane:
            generate_plain_view(lines, print_depth)
        else:
            generate_tree_view(lines, print_depth)
    except (TypeError, FileNotFoundError):
        print("\033[91mError: File Not Found\n指定されたMarkdownファイルが見つかりません。正しいファイルパスを指定してください。\033[0m")
        sys.exit(1)
    except IndexError:
        print("\033[91mError: Empty Heading\nMarkdownファイルから文章のない見出し（#）が検出されました。各見出しには、少なくとも一つの文章を含む必要があります。\033[0m")
