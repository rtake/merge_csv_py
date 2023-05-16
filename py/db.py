import pandas as pd
import sqlite3
import glob

# レシートファイルを読み込んでデータフレームを作成する関数
def read_receipt_file(filename):
    df = pd.read_csv(filename)
    df['File'] = filename  # ファイル名を新たな列に追加
    return df

# ファイルをマージする関数
def merge_files(file_list):
    merged_df = pd.DataFrame()
    for file in file_list:
        df = read_receipt_file(file)
        merged_df = pd.concat([merged_df, df], ignore_index=True)
    return merged_df

# レシートファイルのパスを取得
file_list = glob.glob("./data/user*_receipt.csv")

# ファイルをマージして結果を得る
merged_data = merge_files(file_list)

# SQLiteデータベースに接続
conn = sqlite3.connect("./db/receipts.db")

# データフレームをSQLiteデータベースに挿入
merged_data.to_sql("receipts", conn, if_exists="replace", index=False)

# 接続を閉じる
conn.close()
