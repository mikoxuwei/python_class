import urllib.request as req
# url = 'https://www.ptt.cc/bbs/movie/index.html'
# # 這裡的url是要爬取的網頁,這裡以PTT電影版為例
# url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
def getData(url):
    request = req.Request(url, headers={
        'cookies' : 'over18=1', # 這裡的cookies是用來讓對方網頁以為是已經滿18歲的人在操作
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }) # 以上目的是為了讓對方網頁以為是人在操作

    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')
    # print(data) # 這裡的data是網頁的原始碼

    import bs4
    root = bs4.BeautifulSoup(data, 'html.parser')
    titles = root.find_all('div', class_='title')
    for title in titles:
        if title.a != None:
            print(title.a.string) # 這裡的title.a.string是標題的內容
        else:
            print('No Title') # 這裡的title.a是標題的連結,如果沒有連結就顯示No Title
    nextLink = root.find('a', string='‹ 上頁') # 這裡的nextLink是網頁的上一頁的連結
    # print(nextLink['href']) # 這裡的nextLink['href']是網頁的上一頁的連結
    return nextLink['href'] # 這裡的return是網頁的上一頁的連結,讓下面的程式可以使用
# 抓取一個頁面的標題
pageURL = 'https://www.ptt.cc/bbs/Gossiping/index.html' # 這裡的pageURL是網頁的連結
count = 0 # 計數器,用來計算抓取的頁面數量
while count < 10: # 這裡的count是計數器,用來計算抓取的頁面數量,這裡的5是抓取的頁面數量
    pageURL = 'https://www.ptt.cc' + getData(pageURL) # 這裡的pageURL是網頁的連結,這裡的'https://www.ptt.cc'是網頁的主頁
    print(pageURL) # 這裡的pageURL是網頁的連結
    count += 1 # 計數器加1
# getData(pageURL) # 這裡的getData是抓取網頁的函式,這裡的pageURL是網頁的連結
