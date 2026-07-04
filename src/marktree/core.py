from .exceptions import (
    InputFileNotFoundError,
    InvalidEncodingError,
    InvalidInputError,
    InvalidMarkdownError,
)

def append_tree_branch(depth, name, tree_state, output):
    """
    ツリーの1行を生成して output に追加する。

    Args:
        depth (int): 見出しレベル（# の数）
        name (str): 見出しの名前
        tree_state (dict): 各レベルに見出しが存在するかを記録する辞書
        output (list[str]): 出力用リスト
    """
    line = ""

    for i in range(1, 7):
        if i < depth:
            if tree_state[i] == "exist":
                line += "│  "
            else:
                line += "   "

        elif i == depth:
            if tree_state[i] == "exist":
                line += f"├── {name}"
            else:
                line += f"└── {name}"

            tree_state[i] = "exist"

        else:
            tree_state[i] = "none"

    output.append(line)


def generate_tree(lines, print_depth):
    """
    Markdownテキストを解析し、ツリー形式の文字列を返す。
    """

    tree_state = {i: "none" for i in range(1, 7)}
    output = []

    ignore_code_block = False

    for line in reversed(lines):

        if line.startswith("```"):
            ignore_code_block = not ignore_code_block

        if ignore_code_block:
            continue

        if line.startswith("#"):
            current = line.split(None, 1)

            if len(current) != 2:
                raise InvalidMarkdownError()

            depth = len(current[0])
            name = current[1].rstrip("\n")

            if depth <= print_depth:
                append_tree_branch(depth, name, tree_state, output)

    return "\n".join(reversed(output)) + "\n"


def generate_plain(lines, print_depth):
    """
    見出しをプレーンテキストとして返す。
    """

    output = []

    ignore_code_block = False

    for line in lines:

        if line.startswith("```"):
            ignore_code_block = not ignore_code_block

        if ignore_code_block:
            continue

        if line.startswith("#"):
            current = line.split(None, 1)

            if len(current) != 2:
                raise InvalidMarkdownError()

            depth = len(current[0])

            if depth <= print_depth:
                output.append(line.rstrip("\n"))

    return "\n".join(output) + "\n"


def render_tree(
    filename=None,
    lines=None,
    print_depth=6,
    plain=False,
    encoding="utf-8",
):
    """
    ファイルまたは入力テキストから見出しを読み取り、
    ツリーまたはプレーンテキストを返す。

    Returns:
        str
    """


    if filename is not None:
        try:
            with open(filename, "r", encoding=encoding) as file:
                lines = file.readlines()

        except LookupError as e:
            raise InvalidEncodingError() from e

        except UnicodeDecodeError as e:
            raise InvalidEncodingError() from e

        except FileNotFoundError as e:
            raise InputFileNotFoundError() from e

    if lines is None:
        raise InvalidInputError()

    if plain:
        return generate_plain(lines, print_depth)

    return generate_tree(lines, print_depth)
