# 저장소
import gdown
import pandas as pd
import plotly.express as px

# Google Drive 파일 다운로드 (gdown 사용)
file_url = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'
output = 'data.csv'

# gdown을 사용해 파일 다운로드
gdown.download(file_url, output, quiet=False)

# CSV 파일을 pandas로 읽기
df = pd.read_csv(output)

# 데이터 확인 (Streamlit 사용 시)
import streamlit as st
st.write("### 데이터 미리보기")
st.write(df.head())  # 데이터 첫 5줄을 출력

# Plotly 시각화 예시
fig = px.scatter(df, x='x_column', y='y_column', title="Scatter Plot Example")
st.plotly_chart(fig)

# 시각화 출력
fig.show()
pip install streamlit
import streamlit as st
import pandas as pd
import plotly.express as px
import gdown

# Google Drive 파일 다운로드
file_url = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'
output = 'data.csv'
gdown.download(file_url, output, quiet=False)

# CSV 파일 읽기
df = pd.read_csv(output)

# 데이터 확인
st.write("### 데이터 미리보기")
st.write(df.head())  # 데이터 첫 5줄을 출력

# Plotly 시각화 예시
fig = px.scatter(df, x='x_column', y='y_column', title="Scatter Plot Example")
st.plotly_chart(fig)
streamlit run app.py
git init
git add .
git commit -m "Initial commit"
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin master
streamlit
plotly
pandas
gdown
