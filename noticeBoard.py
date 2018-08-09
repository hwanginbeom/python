import urllib.request
from bs4 import BeautifulSoup
import re
import os

list_url = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp"
detail_url="http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_vie.jsp"

def get_save_path(): #패스를 저장해주는 함수 
    save_path=str(input("저장할 위치와 파일명을 적어주세요 . :"))
    #저장할 위치와 파일명 적기
    scve_path=save_path.replace("\\","/")
    #/이게 있을경우 파이썬 에서 쓰는 \\ 의 형태로 만들어서 경로를 지정해준다.
    
    if not os.path.isdir(os.path.split(save_path)[0]):
        #만약 이폴더가 없을경우 새로 생성해주는 그런 것 같다 이건 찾아 봐야 알 듯
        os.mkdir(os.path.split(save_path)[0])

    return save_path
#save_path를 반환

def fetch_list_url():
    #처음 리스트에서 찾는 것 
    request_header=urllib.parse.urlencode({"page":"1"})
    #페이지를 지정해준다 1-? 사이로 넣을수 있다
    request_header=request_header.encode("utf-8")
    #이 페이지를 넣은것을 utf-8 형태로 만들어서 한글을 볼 수 있게한다.
    url=urllib.request.Request(list_url,request_header)
    #맨위에 넣은 list_url과 헤더 값을 주고 urllib의 기능을 쓰고 그 값을 url에 저장한다.
    res=urllib.request.urlopen(url).read().decode("utf-8")
    #이거 또한 utf-8의 형태로 만들고 읽고 url을 통해 오픈하고 무언가를 요청한다.

    bs=BeautifulSoup(res,"html.parser")
    #res에 담겨있는 내용을 html.parser를 해서 내용을 긁는다 
    listbox=bs.find_all("ul",class_="pclist_list2")
    #parser한 내용 =bs 를 find.all로 내가 원하는 부분을 찾는데
    #그 부분은 ul에 있고 그 속에 class중 pclist 라는 곳에 있다 이 부분을
    # listbox 에 넣는다
    
    #class_= 는  ui 에 대한 속성이라고 말해주는 것
    #해줘도 되고 안해도 되는데 안하면 오류날수도 있어서 해주는게 좋다
    params=[]
    #배열 하나 만들고 
    for i in listbox:
        params.append(re.search("[0-9]{14}",i.find("a")["href"]).group())
    #for문을 돌려서 listbox 의 양 만큼 돌리는데 이때 search를 하고 그 search는
    #숫자 0-9까지의 숫자중에 14자리의 숫자를 가져오는데 이 때
    #i.find로 0~listbox의 갯수 만큼 돌리고 i 에서 href의 a 라는 부분을 가져와서
    #아까만든 params라는 배열에 append로 하나씩 넣어준다. 
    return params
    #그다음 return으로 넣어준다.

def fetch_detail_url():
    #이건 자세한 url부분이다.
    params=fetch_list_url()
    #위에서 한 값을 받아오기 위해 변수를 하나 선언해서 저장하고
    
    f=open(get_save_path(),'w',encoding="utf-8")
    #우리가 파일을 하나 저장해주기 위해 위에 get_save_path()를 쓰고 여기에
    #w를 써서 파일을 새로 저장해준다 이때도 utf-8형식으로 만든다. 

    for p in params:
    # p는 i 와 같은 효과를 하고 여기서 위에서 가져온 처음 기본페이지에서 가져온
    #숫자값을 배열에 넣은 params를 길이 만큼 돌리기 위한 for문이다 
        request_header = urllib.parse.urlencode({"RCEPT_NO":str(p)})
    #여기서 헤더를 만들어주는데 헤더부분은 "RCEPT_NO": ???? 이 물음표는
    #전 페이지에서 하나의 게시글 마다 가지고 있는 고유한 번호를 넣어서 가져오고
    #이 값을 헤더로 넣어주는 방식인것 같다 
    
        
    #헤더는 문자열로 받아야 인식을 한다. 이번호를 고유 번호로 인식하고 해당 페이지를 요청한다
        request_header=request_header.encode("utf-8")
        #이또한 utf-8

        url=urllib.request.Request(detail_url,request_header)
        #detail_url을 header와 같이 넣어서 요청해준다.
        
        res=urllib.request.urlopen(url).read().decode("utf-8")
        #이또한 utf-8로 새로한다 이거 하는 이유는 한글 안깨지게 하기위해

        bs=BeautifulSoup(res,"html.parser")
        #아까와 동일 ( 아마해당 페이지의 전체 html 소스를 가져오는 것 같다.
        div=bs.find("div",class_="form_table")
        #find를 하는데 div중 에 class이름이 form_table이라는 것을 찾아 저장한다.

        tables=div.find_all("table")
        #find_all 로 전체에서 table이라는 것을 가져온다
        info=tables[0].find_all("td")
        #이건 첫번째 테이블로 테이블에서 td라는 부분을 가져온다 

        title=info[0].get_text(strip=True)
        #info가 배열로 되는 이유는 tables가 여러개 여서 그렇고
        #이 0번째 테이블에서는 td가 두개다 그래서 info의 배열이 두개가 나오고
        #그 두가지의 의미가 하나는 title이고 하나는 date이다
        #그 해당 하는 값에 대해 .get_text(strip=True) 를 써서 공백을 없애준다.
        date=info[1].get_text(strip=True)

        question=tables[1].find("div",class_="table_inner_desc").get_text(strip=True)
        #그 테이블에서 또 find를 해서 해당하는 부분가져오고 그 부분에서 공백을 제거한 값을 넣어준다.
        answer=tables[2].find("div",class_="table_inner_desc").get_text(strip=True)

        #이제 우리가 찾은 값을 하나씩써준다. 
        f.write("==" * 30+ "\n")

        f.write(title+ "\n")
        f.write(date+ "\n")
        f.write(question+ "\n")
        f.write(answer+ "\n")

        f.write("==" * 30+ "\n")
        #끄읏
fetch_detail_url()
#프로그램 실행 













        
