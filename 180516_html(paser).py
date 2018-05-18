import requests
from bs4 import BeautifulSoup
def page_download(url):
    response = requests.get(url)
    return response.text

def page_parse(html):
    ret_dict = {}
    parser = BeautifulSoup(html, "html.parser")
    ret_dict["title"] = parser.title.string
    ret_dict["date"] = parser.find('dl', class_="date").find('dd').text.strip()
    ret_dict["writer"] = parser.find('div', class_="writer").text.strip()
    ret_dict["body"] = parser.find('div', class_="contentBody").text.replace("\r\n", " ").strip()

    return ret_dict

if __name__ == '__main__':
    html = page_download("http://www.inven.co.kr/webzine/news/?news=170888&site=overwatch")
    result = page_parse(html)
    for key, value in result.items():
        print(key, ":", value)


