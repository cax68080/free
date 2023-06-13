# 対数表を作る
import pandas as pd
import numpy as np

def create_log_table(base=10):
    #   行方向は0.0から0.9とする
    index = [f"{i}.0" for i in range(1,10)]
    #   列方向は1.0から9.0とする
    columns = [f"0.{j}" for j in range(1,10)]
    #   表を作成する
    table = pd.DataFrame(index=index,columns=columns)
    #   列と行の値の和に対する対数の値を求める
    for i in range(1,10):
        for j in range(10):
            table.at[f"{i}.0",f"0.{j}"] = np.log(i + j * 0.1) / np.log(base)
    return table

#   対数表を作成して表示する
log_table = create_log_table(3)
print(log_table)