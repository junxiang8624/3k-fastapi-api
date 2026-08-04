from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI(title="三國志戰略版 API")

# 允許前端跨網域讀取 (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定義 JSON 檔案路徑（預設放在與 main.py 同目錄下）
JSON_FILE_PATH = "data.json"

def load_game_data():
    """讀取 JSON 檔案的輔助函式"""
    if not os.path.exists(JSON_FILE_PATH):
        # 如果找不到檔案，拋出伺服器錯誤
        raise HTTPException(status_code=500, detail=f"找不到資料檔案: {JSON_FILE_PATH}")
    
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="JSON 檔案格式損毀或錯誤")

@app.get("/")
def read_root():
    return {"status": "success", "message": "三國志戰略版 API 已連線"}

# 1. 取得所有武將資料
@app.get("/api/generals")
def get_all_generals():
    data = load_game_data()
    # 這裡的 "generals" 必須對應您 JSON 裡面的 key 值
    return data.get("generals", [])

# 2. 依據陣營（如：蜀、魏、吳）篩選武將
@app.get("/api/generals/faction/{faction_name}")
def get_generals_by_factor(faction_name: str):
    data = load_game_data()
    generals = data.get("generals", [])
    
    # 篩選出符合陣營的武將（這裡假設您的欄位叫 faction）
    filtered = [g for g in generals if g.get("faction") == faction_name]
    return filtered

# 3. 取得所有戰法資料
@app.get("/api/skills")
def get_all_skills():
    data = load_game_data()
    return data.get("skills", [])