# 실습3. 로또번호추천 챗봇 만들기
# 0.    
import random
# 1. 1~45 숫자가 저장된 numbers 만들기
numbers=range(1,45)
lotto=[]
# 2. 외장함수 random을 활용하여 numbers 배열에서 번호 6개 추출하여 lotto에 저장하기
for i in range(0,6):
    lotto.append(random.choice(numbers))
# 3. lotto 출력하기 
print(lotto)
