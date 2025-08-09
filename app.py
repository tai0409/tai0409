import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
data = {
    'col1': [1, 2, np.nan, 4, 5],
    'col2': ['A', 'B', 'C', 'D', 'A'],
    'col3': [True, False, True, False, True]
}
df = pd.DataFrame(data)

# Hiển thị kiểm tra dữ liệu
st.title("Phân tích dữ liệu mẫu")

st.write("### Kiểm tra giá trị thiếu trong DataFrame:")
st.write(df.isnull().sum())

st.write("### Kiểm tra dòng trùng:")
st.write(df.duplicated().sum())

st.write("### Kiểu dữ liệu của các cột:")
st.write(df.dtypes)

# Vẽ biểu đồ 1: phân bố col1
st.write("### Phân bố col1")
fig1, ax1 = plt.subplots()
sns.histplot(df['col1'], kde=True, color='skyblue', ax=ax1)
ax1.set_xlabel('col1')
ax1.set_ylabel('Tần suất')
st.pyplot(fig1)

# Vẽ biểu đồ 2: phân bố col1 (color orange)
st.write("### Phân bố col1 (color cam)")
fig2, ax2 = plt.subplots()
sns.histplot(df['col1'], kde=True, color='orange', ax=ax2)
ax2.set_xlabel('col1')
ax2.set_ylabel('Tần suất')
st.pyplot(fig2)

# Vẽ biểu đồ 3: mối quan hệ col1 và col3
st.write("### Mối quan hệ giữa col1 và col3")
fig3, ax3 = plt.subplots()
sns.scatterplot(x='col1', y='col3', data=df, color='green', ax=ax3)
st.pyplot(fig3)

# Vẽ biểu đồ 4: ma trận tương quan
st.write("### Ma trận tương quan các biến số")
fig4, ax4 = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax4)
st.pyplot(fig4)

# Vẽ biểu đồ 5: mối quan hệ col1 và col3 (màu tím)
st.write("### Mối quan hệ giữa col1 và col3 (màu tím)")
fig5, ax5 = plt.subplots()
sns.scatterplot(x='col1', y='col3', data=df, color='purple', ax=ax5)
st.pyplot(fig5)
