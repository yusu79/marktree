# =========================
# test_render.py（coreロジックの単体テスト）
# =========================
#
# このテストは CLI を経由せず、
# marktree の中核処理である render_tree() を直接検証する。
#
# 目的は「CLIの外側」ではなく「ロジックそのもの」が正しく動くかを確認すること。
#
# -------------------------
# render_tree の役割
# -------------------------
#
#   render_tree(path)
#
# は Markdown ファイルを解析し、
# 見出し構造をツリー形式に変換するコア関数。
#
# CLIはこの関数を呼び出すだけの薄いラッパーになっている。
#
# -------------------------
# テストの考え方
# -------------------------
#
# このテストでは以下の2種類の結果を検証している：
#
# 1. 正常系
#    → 正しく処理される場合（例: test02〜test06）
#    → result = 0 として扱う
#
# 2. 例外系
#    → 想定されたエラーが発生する場合
#    → 例外クラス名を文字列として取得して比較する
#
# -------------------------
# EXPECTED の意味
# -------------------------
#
#   EXPECTED = {
#       "test01": "InvalidMarkdownError",
#       "test02": 0,
#       ...
#   }
#
# - test01 は不正Markdown → InvalidMarkdownError を期待
# - その他は正常処理 → 0 を期待
#
# -------------------------
# try / except の設計意図
# -------------------------
#
# render_tree() は内部で例外を投げる設計になっているため、
# それをそのまま捕捉して「例外名」を検証対象にしている。
#
# これにより以下が可能になる：
#
# - エラーが正しく分類されているか確認できる
# - CLIに依存せず純粋なロジック検証ができる
#
# -------------------------
# このテストの位置づけ
# -------------------------
#
# test_cli.py    → CLI層（sys.argv / 入出力）
# test_render.py → コアロジック層（render_tree）
#
# 役割を分離することでテストの安定性と保守性を上げている。
# =========================

import pytest
from pathlib import Path

from marktree.core import render_tree

DATA_DIR = Path(__file__).parent / "data"

EXPECTED = {
    "test01": "InvalidMarkdownError",
    "test02": 0,
    "test03": 0,
    "test04": 0,
    "test05": 0,
    "test06": 0,
}

@pytest.mark.parametrize(
    "path",
    sorted(DATA_DIR.glob("*.md"))
)
def test_render(path):
    try:
        render_tree(path)
        result = 0
    except Exception as e:
        result = type(e).__name__

    assert result == EXPECTED[path.stem]
