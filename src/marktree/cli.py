import sys
import os
import pyperclip

from .core import render_tree
from .exceptions import (
    InputFileNotFoundError,
    InvalidEncodingError,
    InvalidInputError,
    InvalidMarkdownError,
)
from .usage import print_usage
from .messages import get_message

# パイプやリダイレクト時も UTF-8 で出力する
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# =========================
# ユーティリティ
# =========================

def get_lang() -> str:
    lang = os.getenv("LANG", "en")
    return "ja" if lang.startswith("ja") else "en"


def print_error(title: str, message: str) -> None:
    BOLD = "\033[1m"
    RED = "\033[91m"
    RESET = "\033[0m"

    print(
        f"{RED}"
        f"[ERROR] {BOLD}{title}{RESET}{RED}\n"
        f"{message}"
        f"{RESET}",
        file=sys.stderr,
    )

# =========================
# エントリーポイント
# =========================
def main():
    lang = get_lang()

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
                print_usage(lang)
                return 0

            elif arg in ["-C", "-c", "--clip"]:
                try:
                    clipboard = pyperclip.paste()
                    options["lines"] = clipboard.split("\r\n") if clipboard else []
                except Exception as e:
                    t, m = get_message(lang, "clipboard_read_failed", error=e)
                    print_error(t, m)
                    return 1
                i += 1

            elif arg == "--copy":
                options["copy"] = True
                i += 1

            elif arg in ["-L", "-l", "--level"]:
                try:
                    options["print_depth"] = int(sys.argv[i + 1])
                except IndexError:
                    t, m = get_message(lang, "missing_level")
                    print_error(t, m)
                    return 1
                except ValueError:
                    t, m = get_message(lang, "invalid_level")
                    print_error(t, m)
                    return 1
                i += 2

            elif arg in ["-P", "-p", "--plain"]:
                options["plain"] = True
                i += 1

            elif arg in ["-E", "-e", "--encoding"]:
                try:
                    options["encoding"] = sys.argv[i + 1]
                except IndexError:
                    t, m = get_message(lang, "missing_encoding")
                    print_error(t, m)
                    return 1
                i += 2

            elif arg.startswith("-"):
                t, m = get_message(lang, "invalid_option")
                print_error(t, m)
                return 1

            else:
                options["filename"] = arg
                i += 1

    except Exception as e:
        t, m = get_message(lang, "unexpected_error", error=e)
        print_error(t, m)
        return 1

    depth = options["print_depth"]
    if not 1 <= depth <= 6:
        t, m = get_message(lang, "level_out_of_range")
        print_error(t, m)
        return 1

    copy = options.pop("copy")

    try:
        text = render_tree(**options)

    except InputFileNotFoundError:
        t, m = get_message(lang, "file_not_found")
        print_error(t, m)
        return 1

    except InvalidEncodingError:
        t, m = get_message(lang, "invalid_encoding")
        print_error(t, m)
        return 1

    except InvalidInputError:
        t, m = get_message(lang, "invalid_input")
        print_error(t, m)
        return 1

    except InvalidMarkdownError:
        t, m = get_message(lang, "empty_heading")
        print_error(t, m)
        return 1

    if copy:
        pyperclip.copy(text)
    else:
        print(text, end="")


    return 0
