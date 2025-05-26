# 저장소
import pandas as pd
import plotly.express as px
import gdown

# 1. Google Drive 파일 다운로드
file_url = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'
output = 'data.csv'  # 다운로드한 파일을 저장할 로컬 경로
gdown.download(file_url, output, quiet=False)

# 2. CSV 파일을 pandas로 읽기
df = pd.read_csv(output)

# 데이터 확인
print(df.head())  # 데이터를 미리 확인

# 3. Plotly로 시각화하기
# 예시로, 데이터에 'x'와 'y' 컬럼이 있다고 가정하고 산점도 (scatter plot) 만들기
fig = px.scatter(df, x='x_column', y='y_column', title="Scatter Plot Example")

# 시각화 결과 출력
fig.show()
