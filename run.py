#Thiều Minh Thành - 2321050015
#Đào Duy Đức - 2321050088
#Nguyễn Trung Đức - 2321050091
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
movies_data = pd.read_csv(
    "https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv"
)
movies_data.dropna(inplace=True)

# Sidebar - Widgets
st.sidebar.header("Select a range on the slider (it represents movie score)")
score_range = st.sidebar.slider("Choose a value:", min_value=1.0, max_value=10.0, value=(1.0, 10.0), step=0.1)

genre_options = movies_data['genre'].unique().tolist()
selected_genres = st.sidebar.multiselect("Choose Genre:", genre_options, default=genre_options[:4])

years = sorted(movies_data['year'].dropna().unique())
selected_year = st.sidebar.selectbox("Choose a Year", years)

# Lọc dữ liệu
filtered_data = movies_data[
    (movies_data['score'] >= score_range[0]) &
    (movies_data['score'] <= score_range[1]) &
    (movies_data['genre'].isin(selected_genres)) &
    (movies_data['year'] == selected_year)
]

# Giao diện chính
st.title("Interactive Dashboard")
st.write("Interact with this dashboard using the widgets on the sidebar")

# Hiển thị bảng dữ liệu
st.subheader("Lists of movies filtered by year and Genre")
st.dataframe(filtered_data[['name', 'genre', 'year']])

# Biểu đồ cột - điểm theo thể loại
st.subheader("User score of movies and their genre")

score_by_genre = filtered_data.groupby('genre')['score'].mean().sort_values()
# Tạo biểu đồ cột
plt.figure(figsize=(8,5))
plt.bar(score_by_genre.index, score_by_genre.values, color='skyblue')
# Thêm nhãn và tiêu đề
plt.xlabel('Thể loại phim')
plt.ylabel('Điểm trung bình')
plt.title('Biểu đồ điểm trung bình theo thể loại')
plt.xticks(rotation=30)

st.pyplot()
