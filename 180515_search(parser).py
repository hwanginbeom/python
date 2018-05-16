import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def spider(max_pages):
    page=1
    max_pages=5
    while page < max_pages:
        url=["https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL6omwAg&q=L’AsduFallafel",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL7omwAg&q=Ladurée",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL8omwAg&q=Angelina",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL9omwAg&q=BouillonChartier",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL10omwAg&q=Berthillon"
]

        source_code = requests.get(url[page])
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        for link in soup.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]'):
            href = url[page] + link.get
            title = link.string
            print(href)
            print(title)

        page +=1

spider(5)
