from textblob import TextBlob
import tkinter as tk
from PIL import Image, ImageTk
import os

# GUI 設定
window = tk.Tk()
window.title("共感機體：情緒互動模擬")
window.geometry("500x600")

# 圖片檔案對應情緒
emotion_images = {
    "positive": "happy.png",
    "negative": "sad.png",
    "neutral": "neutral.png"
}

# 表情圖片顯示元件
image_label = tk.Label(window)
image_label.pack(pady=10)

# 顯示圖片
def show_emotion_image(emotion):
    img_path = os.path.join("C:/python/AI", emotion_images[emotion])
    img = Image.open(img_path)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    image_label.configure(image=img_tk)
    image_label.image = img_tk

# 回應顯示區域
response_label = tk.Label(window, text="", font=("Arial", 12), wraplength=450)
response_label.pack(pady=10)

# 輸入區域
entry = tk.Entry(window, width=60)
entry.pack(pady=10)

# 關鍵字列表（中文）
positive_keywords = ["開心", "快樂", "幸福", "讚", "喜歡", "棒", "感謝"]
negative_keywords = ["煩", "難過", "討厭", "壓力", "哭", "累", "爛", "生氣", "不爽", "不開心"]
neutral_keywords = ["還好", "普通", "平靜"]

# 情緒分析函數
def analyze_emotion():
    text = entry.get()
    text_lower = text.lower()

    # 中文關鍵字優先分析
    emotion = "neutral"
    response = "你說的話聽起來很平靜。"

    for kw in positive_keywords:
        if kw in text:
            emotion = "positive"
            response = "聽起來你今天很不錯，繼續保持好心情！"
            break
    for kw in negative_keywords:
        if kw in text:
            emotion = "negative"
            response = "感覺你有點低落，希望你一切都好。"
            break

    # 如果是英文句子 → 使用 TextBlob 當備用
    if all(ord(c) < 128 for c in text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            emotion = "positive"
            response = "You sound great today. Keep it up!"
        elif polarity < -0.1:
            emotion = "negative"
            response = "Sounds like a tough day. Hope it gets better."
        else:
            emotion = "neutral"
            response = "That sounds quite calm."

    # 顯示結果
    show_emotion_image(emotion)
    response_label.config(text=f"[系統分析：{emotion}]\n{response}")

# 送出按鈕
analyze_btn = tk.Button(window, text="送出", command=analyze_emotion)
analyze_btn.pack(pady=10)

window.mainloop()
