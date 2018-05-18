import requests
from bs4 import BeautifulSoup

urls=["https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Brasserie Balzar",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Kheak & Vero",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+O’Scia",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Café Marlette",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Sapporo",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Les Fables de la Fontaine",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Unico",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Cigale Récamier",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Cafe Rive Droite",
]

values=0
a=0

def page_download(url):
    response = requests.get(url)
    return response.text

def page_parse(html):
    ret_dict = {}
    parser = BeautifulSoup(html, "html.parser")
    ret_dict["review"] = parser.find('div', class_= "slp").text.strip()
    
    #print(a)


    return ret_dict

while values < 150:
    if __name__ == '__main__':
        html = page_download(urls[values])
        result = page_parse(html)
        for key, value in result.items():
            print(key, ":", value)
            values +=1
            a +=1
            


