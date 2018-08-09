import urllib.parse
import urllib.request
import re 

def input_query( ):
   q = urllib.parse.quote_plus(str(input("검색할 단어를 입력하세요: ")))
   return "&query=" + q

def bind_url( ) :
    default_url = 'https://openapi.naver.com/v1/search/image.xml?'
    start = '&start=1'
    sort = '&sort=sim'
    display = '&display=10'
    query = '&query='+urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))
    full_url = default_url + sort + start + display + query
    print(full_url)
    return full_url

def fetch_contents_from_url( ):
    url = bind_url( )
    headers = {
     'Host' : 'openapi.naver.com',
     'User-Agent' : 'curl/7.43.0',
     'Accept' : '*/*',
     'Content-Type' : 'application/xml',
     'X-Naver-Client-Id' : 'nudvF5h65mkwQojGKFoS',
     'X-Naver-Client-Secret' : 'GkT_LfiAa_'
     }
    r = urllib.request.Request(url,headers=headers)
    m = urllib.request.urlopen(r)
    html = m.read( )
    return html

def extract_text_in_tags(tags,tagname=" "):
    txt=[] #배열
    reg="[^<"+tagname+">][^<]+" # ^<이부분 제외하고 찾는데 ][^<] 이부분 나오면 끝 그래서 text만 가져온다
    #print(reg)
    for tag in tags: # for문 돌리는데 tag
        txt.append(re.search(reg,tag).group() )# txt에 하나씩 추가한다 search
    print(txt)
    return txt

def get_contents_from_html():
    html = fetch_contents_from_url()
    #print(html.decode('utf-8'))
    #print(html)
    title_tags=re.findall("<title>[^<]+</title>",html.decode('utf-8'))#찾는다 title 에서 /title 부분까지 가져온다. 그걸 title_tags에 넣는다
    link_tags=re.findall("<link>[^<]+</link>",html.decode('utf-8'))
    print(link_tags)
    print(title_tags)

    titles=extract_text_in_tags(title_tags,tagname="title")
    links = extract_text_in_tags(link_tags,tagname='link')
    f=open("image.html","w")
    f.write("<html><body>")
    for i in range(1,len(titles)):
        f.write("<p>"+titles[i]+"</p>")
        f.write("<img src="+links[i]+"/>")
    f.write("</body></html>")
    f.close()

get_contents_from_html()











