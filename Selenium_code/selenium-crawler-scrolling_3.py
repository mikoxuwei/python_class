import requests
from bs4 import BeautifulSoup

# 設定要爬取的網址
url = 'https://www.awwwards.com/sites/who-is-guilty#google_vignettw'

# 發送 GET 請求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

# 確認請求成功
if response.status_code != 200:
    print("無法成功載入頁面，狀態碼:", response.status_code)
    exit()

# 解析 HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 定義要擷取的標籤類型
heading_tags = ['h1', 'h2', 'h3']
results = []  # 儲存擷取的資料
# 逐一擷取各種標籤的文字
for tag in heading_tags:
    headings = soup.find_all(tag)  # 根據標籤名稱擷取元素
    for heading in headings:
        heading_text = heading.get_text(strip=True)  # 擷取文字並去除前後空白
        if not heading_text:  # 確保文字不為空
            continue
        # 嘗試取得 heading 所在父元素中的內文段落
        paragraph_texts = []
        parent = heading.find_parent()
        if parent:
            paragraphs = parent.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text:
                    paragraph_texts.append(text)

        results.append((heading_text, paragraph_texts))
# 印出擷取的文字
for title, paragraphs in results:
    print(f"🔹 標題:{title}")
    if paragraphs:
        for para in paragraphs:
            print(f"    -內文:{para}")
    else:
        print("    -內文:無")
    print()
# 關閉瀏覽器
driver.quit()