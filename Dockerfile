# 1. 使用官方輕量版 Python 映像檔
FROM python:3.10-slim

# 2. 設定容器內的工作目錄
WORKDIR /app

# 3. 先複製套件清單並安裝，利用 Docker 快取機制加速未來建立速度
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 複製目前目錄下的所有程式碼與資料（包含 main.py 和 data.json）到容器中
COPY . .

# 5. 開放容器的 8000 埠號
EXPOSE 8000

# 6. 啟動伺服器指令（注意：雲端部署時不需要 --reload，且 host 必須設定為 0.0.0.0）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
