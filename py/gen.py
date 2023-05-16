import random

foods = ["pork", "onion", "apple", "milk", "egg", "bread", "rice", "tomato", "carrot", "chicken"]

# ファイルを生成する関数
def generate_file(file_number):
    filename = f"./data/user{file_number:02d}_receipt.csv"
    with open(filename, "w") as file:
        file.write("Food,Price\n")  # ヘッダー行を書き込む
        selected_foods = random.sample(foods, random.randint(1, len(foods)))
        for food in selected_foods:
            price = random.randint(100, 1000)
            record = f"{food},{price}\n"
            file.write(record)

# 10個のファイルを生成する
for i in range(1, 11):
    generate_file(i)
