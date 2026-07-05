from pathlib import Path
import pytest

from marktree.core import render_tree

DATA_DIR = Path(__file__).parent / "data"
EXPECTED_DIR = Path(__file__).parent / "expected"


@pytest.mark.parametrize(
    "path",
    sorted(DATA_DIR.glob("*.md"))
)
def test_render(path):
    expected = (
        EXPECTED_DIR / f"{path.stem}.txt"
    ).read_text(encoding="utf-8").strip()

    try:
        render_tree(path)
        result = "ok"
    except Exception as e:
        result = type(e).__name__


    assert result == expected
