import pandas as pd
import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0) Gecko/20141222 Firefox/35.0'}

# 一共有10页
base_url = 'https://book.douban.com/top250?start={}'

result = pd.DataFrame()
for num in range(0, 250, 25):
    url = base_url.format(num)
    html = requests.get(url, headers=headers)
    print(html.status_code)
    bs = etree.HTML(html.text)
    for i in bs.xpath('//tr[@class = "item"]'):
        # 书籍中文名
        book_ch_name = i.xpath('td[2]/div[1]/a[1]/@title')[0]
        # 评分
        score = i.xpath('td[2]/div[2]/span[2]')[0].text
        # 书籍信息
        book_info = i.xpath('td[2]/p[@class = "pl"]')[0].text
        # 评价数量由于数据不规整，这里用PYTHON字符串方法对数据进行了处理
        comment_num = i.xpath(
            'td[2]/div[2]/span[3]')[0].text.replace(' ', '').strip('(\n').strip('\n)')
        # 书籍封面
        back = i.xpath('td[1]/a/img/@src')[0]
        try:
            # 后面有许多书籍没有一句话概括
            # 一句话概括
            brief = i.xpath('td[2]/p[@class = "quote"]/span')[0].text
        except:
            brief = None
        # 这里的cache是存储每一次循环的结果，然后通过下一步操作循环更新result里面的数据
        cache = pd.DataFrame({'中文名': [book_ch_name], '评分': [score], '封面': [back],
                              '书籍信息': [book_info], '评价数量': [comment_num], '一句话概括': [brief]})
        # 把新循环中的cache添加到result下面
        result = pd.concat([result, cache])
    print('我们正在爬取：{}页'.format((num / 25) + 1))
    time.sleep(40)

result.head()
# 把结果一步存为EXCEL
result.to_excel('豆瓣图书TOP250.xlsx', index=False)

'''保存图片至本地
data = pd.read_excel("./豆瓣图书TOP250.xlsx", usecols=[0, 2])
i = 0
for name, url in data.values:
    i += 1
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content
        with open(f"./images/{name}.jpg", "wb") as file:
            file.write(text)
        print(f"已保存{i}张，还剩{250-i}张封面")
        time.sleep(3)
    else:
        print("Error occur!")
        break
print("已获取全部封面！")
'''


def process(string):
    data = string.replace(" ", "").split("/")
    size = len(data)
    if size == 4:
        pass
    elif size == 5:
        data = [", ".join(data[:2])+"(译)", data[2], data[3], data[4]]
    elif size == 6:
        data = [", ".join(data[:2])+"(译)", data[2], data[3],
                ", ".join(data[4:])+"(译本)"]
    return data
