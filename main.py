import crawler
import data_clear
import pandas as pd

# 2014 ~ 2021
xpath_list = ['/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/ul/div/button[34]',
              '/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/ul/div/button[35]',
              '/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/ul/div/button[36]',
              '/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/ul/div/button[37]',
              '/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/ul/div/button[38]',
              '/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/ul/div/button[39]',
              '/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/ul/div/button[40]',
              '/html/body/div[1]/div[1]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/ul/div/button[41]']

crawling_list = []

for x in xpath_list:
    crawling_list.append(crawler(x))

# dataframe에 사용할 컬럼명 list로 선언
record_col = ['순', '이름', '팀', '정렬', '출장', '완투', '완봉', '선발', '승', '패', '세', '홀드', '이닝', '실점', '자책', '타자', '안타', '2타', '3타', '홈런', '볼넷', '고4', '사구', '삼진', '보크', '폭투', 'ERA', 'FIP', 'WHIP', 'ERA+', 'FIP+', 'WPA', 'WAR']

# 컬럼만 있는 빈 데이터프레임 생성
pitch_df = pd.DataFrame(columns=record_col)
pitch_df

for c in crawling_list:
    df = data_clear(c)
    pitch_df = pd.concat([pitch_df, df])