# 親ディレクトリをパスに追加することで、後段の親ディレクトリのモジュール import を可能とする
import sys
import pathlib
parent_dir = str(pathlib.Path(__file__).parent.parent.resolve())
sys.path.append(parent_dir)

# VSCode の pylint ではエラーがでるが、実行には問題なし
import parent

print(parent)
print(parent.val)
