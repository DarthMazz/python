from multiprocessing import Pipe, Process
import time


def f3(conn):
    # time.sleep(1)
    # パイプにデータを送信します.
    # conn.send({"age": 30, "name": "Yohei"})
    # a = ""
    # for i in range(10000000):
    #     a += "a"
    # conn.send(a)
    # パイプをクローズします.
    # conn.close()

    # クローズ後に書き込もうとすると、エラーになります（OSError: handle is closed）.
    # conn.send([42, None, "Hello"])
    with open("./3.jpg", mode="rb") as f:
        image_byte = f.read()
        conn.send(image_byte)


if __name__ == "__main__":
    # Pipeを生成します（デフォルトでは双方向にやり取りできるパイプ）
    # 双方向にやり取りできますが、両端で自由に読み書きしているとデータが壊れる可能性があるので、
    # 基本的にはどちらかを書き込み専用、どちらかを読み込み専用に扱います.
    parent_conn, child_conn = Pipe()
    # Pipeの片方の端を、サブプロセスに渡します.
    p = Process(target=f3, args=(child_conn,))
    # サブプロセスを開始します.
    p.start()
    # Pipeから値が取得できるまで待ちます.
    # print(parent_conn.recv())
    with open("./33.jpg", mode="wb") as f:
        f.write(parent_conn.recv())
    # サブプロセスの終了を待ちます.
    p.join()
