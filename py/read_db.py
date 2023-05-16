import sqlite3
import pandas as pd

# SQLiteデータベースファイルに接続
conn = sqlite3.connect("./db/receipts.db")

# SQLクエリを実行して結果をDataFrameに変換
query = "SELECT * FROM receipts"
df = pd.read_sql_query(query, conn)

# 接続を閉じる
conn.close()

# DataFrameを表示
print(df)
