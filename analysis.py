import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel("年度数据.xlsx")

years = [2021, 2022, 2023, 2024, 2025]
sales = [438351.9, 436448.7, 467098.0, 483344.7, 501202.0]

data = pd.DataFrame({
    "年份": years,
    "社会消费品零售总额(亿元)": sales
})

data["同比增长率(%)"] = data["社会消费品零售总额(亿元)"].pct_change() * 100

print("===== 社会消费品零售总额分析结果 =====")
print(data)

plt.figure(figsize=(10, 6))
plt.bar(data["年份"], data["社会消费品零售总额(亿元)"], color="#1f77b4", alpha=0.8, label="零售总额")

for i, value in enumerate(data["社会消费品零售总额(亿元)"]):
    plt.text(data["年份"][i], value + 5000, f"{value}", ha="center", fontsize=10)

plt.title("2021-2025年中国社会消费品零售总额趋势分析", fontsize=14)
plt.xlabel("年份", fontsize=12)
plt.ylabel("零售总额(亿元)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.legend()

plt.savefig("零售总额分析图.png", dpi=300, bbox_inches="tight")
plt.show()

print("\n分析完成！图表已保存为 零售总额分析图.png")
