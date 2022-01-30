import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
import warnings
warnings.filterwarnings('ignore')

def crawler(year_xpath):
    # Chromedriver 옵션 설정
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=976,1056")

    # execute driver & connect page
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get('http://www.statiz.co.kr/stat.php?re=1&lr=0')
    time.sleep(3)

    # 스크롤을 위한 ActionChains 모듈 선언
    action = ActionChains(driver)
    
    # 연도 옵션 설정
    yearbutton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/button')
    time.sleep(2)
    yearbutton.click()
    
    # 연도 지정
    time.sleep(2)
    year_select = driver.find_element_by_xpath(year_xpath)
    driver.execute_script("window.scrollTo(0, 200);") # 광고로 인해 옵션버튼이 가려질 수 있으므로
    year_text = year_select.text
    year_select.click()
    
    # 100개씩 정렬하기 위한 옵션설정
    optionbutton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[8]/button')
    driver.execute_script("window.scrollTo(0, 100);") # 광고로 인해 옵션버튼이 가려질 수 있으므로
    time.sleep(2)
    optionbutton.click()

    # 정렬 개수 100개로 설정
    print_num = Select(driver.find_element_by_xpath('//*[@id="opt_div"]/div[2]/div[5]/form/select'))
    print_num.select_by_value('100')

    # 첫번째 다음버튼 선언 (2페이지부터는 '이전'버튼이 생겨 xpath가 바뀜)
    if year_text == '21':
        first_nextbutton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[6]/div/div/div[4]/table/tbody/tr/td[2]/a[2]')
    else:
        first_nextbutton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[5]/div/div/div[4]/table/tbody/tr/td[2]/a[2]')
        
    p_list = []
    count = 0
    while True:
        player = driver.find_element_by_id('mytable') # 크롤링 대상인 지표만을 선정
        count += 1
        for p in player.find_elements_by_tag_name('tr'):
            record = p.text
            p_list.append(record.split()) # 한 선수마다 하나의 list로 만들어서 저장
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 맨 아래까지 스크롤, 광고로 가려짐을 피하기 위해
        if year_text == '21':
            nextbutton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[6]/div/div/div[4]/table/tbody/tr/td[2]/a[3]')
        else :
            nextbutton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[5]/div/div/div[4]/table/tbody/tr/td[2]/a[3]')
        time.sleep(2)
        if count == 1: # 첫 번째 페이지일 때
            first_nextbutton.click()
            time.sleep(2)
        else: # 두 번째 페이지 이상일 때
            if nextbutton.text == '마지막':
                print(count, '페이지 수집완료.')
                break
            nextbutton.click()
            time.sleep(2)
            
    return p_list