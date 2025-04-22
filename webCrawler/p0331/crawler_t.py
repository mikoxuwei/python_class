# 0331(PTT八卦版) grab the source codes of PTT movie website
import urllib.request as req
def getData(url):
    # set a request object and attach the data of Request Headers
    request= req.Request(url, headers= {
        'cookies': 'over18=1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    })  
# 以上作業的目的為讓對方網頁以為是人(非機器)在操作

    with req.urlopen(request) as response:
        data= response.read().decode('utf-8')
    print(data)  # 印出原始碼(檢測是否連線成功?)

    # 解析原始碼並抓取標題
    import bs4
    root= bs4.BeautifulSoup(data, 'html.parser')
    # 搜尋 title 前面有 div 字串
    titles= root.find_all('div', class_= 'title')  
    for title in titles:
         if title.a != None:  # 如果每一行的抬頭有包含 a 就印出
             print(title.a.string)
         else:
            print('No Title') # 這裡的title.a是標題的連結,如果沒有連結就顯示No Title

    # grab nextpage linkage 抓取到下一頁的連結網址
    # 搜尋有 '< 上頁' a 字串的行
    nextLink = root.find('a', string= '< 上頁')
    return nextLink['href']  # 回傳上頁的網址
# Grab a page title
pageURL= 'https://www.ptt.cc/bbs/Gossiping/index.html'
count= 0
while count<10:
      pageURL= 'https://www.ptt.cc' + getData(pageURL)
      count+=1