import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")
movies_data = movies_data.dropna()

# Tính ngân sách trung bình theo thể loại
avg_budget = movies_data.groupby('genre')['budget'].mean().round().reset_index()

# Dữ liệu
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

# Vẽ biểu đồ PIE
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(avg_bud, labels=genre, autopct='%1.1f%%', startangle=140)
ax.set_title("Tỷ lệ ngân sách trung bình theo thể loại phim")

# Hiển thị lên Streamlit
st.title("Biểu đồ Tỷ lệ Ngân sách theo Thể loại")
st.pyplot(fig)