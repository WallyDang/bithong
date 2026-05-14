import pandas as pd
import matplotlib.pyplot as plt

# Đọc trực tiếp file CSV
df = pd.read_csv("SDnobel.csv")

# Đếm số lượng theo loại laureate
type_data = (
    df.groupby("laureate_type")
      .size()
      .reset_index(name="count")
)

# Màu cho từng loại
colors = {
    "Individual": "#3498db",
    "Organization": "#e67e22"
}

# Tạo biểu đồ
plt.figure(figsize=(8, 5))

plt.bar(
    type_data["laureate_type"],
    type_data["count"],
    color=[colors.get(x, "#95a5a6") for x in type_data["laureate_type"]]
)

# Tiêu đề và nhãn
plt.title("Nobel Laureates by Type", fontsize=16, fontweight="bold")
plt.xlabel("Laureate Type")
plt.ylabel("Total Count")

# Giao diện tối giản
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()
