import urllib.request

# 1. SAS URL을 통해 Titanic CSV 파일 다운로드
file_url = "https://<your_blob_url_with_sas_token>"
local_path = "/tmp/titanic.csv"
urllib.request.urlretrieve(file_url, local_path)

# 2. PySpark로 CSV 불러오기
df = spark.read.option("header", "true").csv(f"file:{local_path}")

# 3. 상위 5개 행 미리보기
df.show(5)
