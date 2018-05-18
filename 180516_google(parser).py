import requests
from bs4 import BeautifulSoup

urls=["https://www.google.co.kr/search?source=hp&ei=soz7Ws6FIoKE8wXUkI6ABA&q=L%E2%80%99As+du+Fallafel&oq=&gs_l="
      ,"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL7omwAg&q=Ladurée",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL8omwAg&q=Angelina",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL9omwAg&q=BouillonChartier",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL11omwAg&q=ComptoirdelaGastronomie",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL12omwAg&q=PierreHermé",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL13omwAg&q=L’AvantComptoir",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL14omwAg&q=BlueElephant",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL15omwAg&q=Kong"
]

values=0

def page_download(url):
    response = requests.get(url)
    return response.text

def page_parse(html):
    ret_dict = {}
    parser = BeautifulSoup(html, "html.parser")
    ret_dict["review"] = parser.find('div', class_= "mod").text.strip()


    return ret_dict

while values < 9:
    if __name__ == '__main__':
        html = page_download(urls[values])
        result = page_parse(html)
        for key, value in result.items():
            print(key, ":", value)
            values +=1


