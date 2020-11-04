# 親ディレクトリをパスに追加することで、後段の親ディレクトリのモジュール import を可能とする
import sys
import pathlib
parent_dir = str(pathlib.Path(__file__).parent.parent.resolve())
sys.path.append(parent_dir)

# VSCode の pylint ではエラーがでるが、実行には問題なし
from main.calc import Calc


def test_add_01():
    assert Calc(9, 2).add() == 11


def test_sub_01():
    assert Calc(9, 2).sub() == 7


def test_mul_01():
    assert Calc(9, 2).mul() == 18


def test_div_01():
    assert Calc(8, 2).div() == 4


def test_div_02():
    assert Calc(8, 0).div() == "Not Divide"
