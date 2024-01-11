import sys

def usage():
    print("""
Usage: marktree [-h|--help] [-L|-l|--level level] [foo.md]

Description: convert headings in a Markdown file (.md) into a tree-like structure and output.

Arguments:
    foo.md           Pass the Markdown file for which you want to output headings in a tree.

Options:
    -h|--help          Display help
       --help_jp       Display help in Japanese
    -L|-l|--level      Display headings up to the specified level (default is "6")

""")
def usage_jp():
    print("""
使用法: marktree [-h|--help] [-L|-l|--level 階層] [hoge.md]

説明: Markdownファイル（.md）の見出しを木構造で表示するコマンド

引数:
    hoge.md           木構造で表示したいMarkdownファイルを引数に指定します。

オプション:
    -h|--help         ヘルプを表示します
       --help_jp      日本語のヘルプを表示します
    -L|-l|--level     指定した階層までの見出しを表示します（デフォルトは「6」）

""")

def print_branch(depth, name, dict, output):
    mozi=""
    for i in range(1, 7):
        if i < depth:
            if dict[i] == "exist":
                mozi+="│  "
            else:
                mozi+="   "
        elif i == depth:
            if dict[i] == "exist":
                mozi+=f"├── {name}"
            else:
                mozi+=f"└── {name}"
            dict[i] = "exist"
        else:
            dict[i] = "none"
    output.append(mozi)


def print_tree(filename, print_depth):
    current_depth = 0
    current_name = ""
    dict = {
        1: "none",
        2: "none",
        3: "none",
        4: "none",
        5: "none",
        6: "none"
    }
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            output=[]
            for line in reversed(lines):
                if line.startswith('#') :
                    current = line.split(None, 1)
                    current_depth = len(current[0])
                    current_name = current[1].strip("\n")
                    if current_depth <= print_depth:
                        print_branch(current_depth, current_name, dict, output)

            for i in reversed(output):
                print(i)
            print("")
    except (TypeError,FileNotFoundError):
        print("\033[91mError: File Not Found\n指定されたMarkdownファイルが見つかりません。正しいファイルパスを指定してください。\033[0m")
        sys.exit(1) 
    except IndexError:
        print("\033[91mError: Empty Heading\nMarkdownファイルに文章のない見出し（#）が検出されました。各見出しは少なくとも一つの文章を含む必要があります。\033[0m")


def main():
    filename = None
    print_depth = 6

    i = 1
    # ファイル名も階層も上書きするので、引数はいくら渡してもいい
    try:
        while i < len(sys.argv):
            if sys.argv[i] in ["-h", "--help"]:
                usage()
                sys.exit(0)
            elif sys.argv[i] in ["--help_jp"]:
                usage_jp()
                sys.exit(0)
            elif sys.argv[i] in ["-L", "-l", "--level"]:
                print_depth = int(sys.argv[i + 1]) # 階層は上書き
                i += 2
            elif sys.argv[i].startswith("-"):
                print("\033[91mError: Invalid Option\n無効なオプションです。--help を使用してください。\033[0m")
                sys.exit(1)
            else:
                filename = sys.argv[i] # ファイル名は上書き
                i += 1
    except ValueError:
        print("\033[91mError: Invalid Hierarchy Level\n階層には正の整数を指定してください。例: -L 2\033[0m")
        sys.exit(1)
    except IndexError: # -Lの直後に階層が指定されない時はデフォルト値（6）
        pass

    if print_depth < 1 or print_depth > 6:
        print("\033[91mError: Hierarchy Level Out of Range\n階層は1から6までの間で指定してください。\033[0m")
        sys.exit(1)


    return print_tree(filename,print_depth)


