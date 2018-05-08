from selenium import webdriver

# 유의: chromedriver를 위에서 받아준 
# chromdriver(windows는 chromedriver.exe)의 절대경로로 바꿔주세요!
driver = webdriver.Chrome('C:/Users/user/Downloads/AnySign_Installer.exechromedriver_win32/chomedriver')

driver.get('http://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main.png')

driver.quit()
