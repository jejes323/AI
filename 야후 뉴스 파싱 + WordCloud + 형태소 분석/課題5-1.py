
import pandas as pd
df=pd.read_csv('/content/drive/MyDrive/AI/miyajima_sample.csv', encoding='utf8',parse_dates=['旅行の時期'])

# ★ 月ごとの口コミ件数を数える
month_count = {}  # {月: 件数}

for date in df["旅行の時期"]:  # Timestamp が1行ずつ取り出される
    month = date.month        # 月を取得
    if month not in month_count:
        month_count[month] = 0
    month_count[month] += 1

# ★ 結果を標準出力（print）
print("月ごとの口コミ件数：")
for month in sorted(month_count.keys()):
    print(f"{month}月: {month_count[month]} 件")
