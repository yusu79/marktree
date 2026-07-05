# =========================
# test_cli.py（CLIテストの仕組み）
# =========================
#
# このテストは subprocess を使わず、
# pytest の monkeypatch を利用して CLI の入力を疑似的に再現している。
#
# 通常 CLI は以下のように実行される：
#
#   marktree test.md
#
# このとき Python 内部では sys.argv が次のようになっている：
#
#   sys.argv = ["marktree", "test.md"]
#
# しかしテスト環境では実際にコマンドを実行しないため、
# monkeypatch を使って sys.argv を強制的に書き換える。
#
# -------------------------
# monkeypatch の役割
# -------------------------
#
#   monkeypatch.setattr("sys.argv", ["marktree", str(path)])
#
# これはテスト中だけ sys.argv を置き換える処理であり、
# 「CLIコマンドが実行された状態」を人工的に作っている。
#
# その結果、main() は本物のCLIと同じように振る舞う。
#
# -------------------------
# main() の動作
# -------------------------
#
#   result = main()
#
# main() は sys.argv を参照して処理を行うため、
# monkeypatch によって差し替えられた引数を使って実行される。
#
# -------------------------
# この方式のメリット
# -------------------------
#
# - subprocess を使わないため高速
# - OS依存（Windowsのcp932など）の問題を回避できる
# - CLI本体と同じ処理経路を通るため信頼性が高い
#
# -------------------------
# EXPECTED の意味
# -------------------------
#
#   EXPECTED[path.stem]
#
# は各テストファイルに対して期待される終了コードを定義している。
# 例えば：
#
#   test01 → エラー → 1
#   test02 → 正常 → 0
#
# =========================

import pytest
from pathlib import Path

from marktree.cli import main

DATA_DIR = Path(__file__).parent / "data"

EXPECTED = {
    "test01": 1,
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
def test_cli(monkeypatch, path):
    monkeypatch.setattr(
        "sys.argv",
        ["marktree", str(path)]
    )

    result = main()

    assert result == EXPECTED[path.stem]


