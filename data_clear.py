import numpy as np
import pandas as pd

def data_clear(crawling_list) :
    # 10명의 기록마다 컬럼명이 새로 생기므로 이를 없애줌
    while True:
        try:
            crawling_list.remove(['순', '이름', '팀', '정렬', '출장', '완투', '완봉', '선발', '승', '패', '세', '홀드', '이닝', '실점', '자책', '타자', '안타', '2타', '3타', '홈런', '볼넷', '고4', '사구', '삼진', '보크', '폭투', '비율', 'WAR', 'WPA'])
            crawling_list.remove(['WAR', 'ERA', 'FIP', 'WHIP', 'ERA+', 'FIP+'])
        except:
            print('삭제완료')
            break
        
    
    remove_list = []
    
    for c in crawling_list:
        if len(c) < 33:
            remove_list.append(c)
            
    for r in remove_list:
        crawling_list.remove(r)
        
    # dataframe에 사용할 컬럼명 list로 선언
    record_col = ['순', '이름', '팀', '정렬', '출장', '완투', '완봉', '선발', '승', '패', '세', '홀드', '이닝', '실점', '자책', '타자', '안타', '2타', '3타', '홈런', '볼넷', '고4', '사구', '삼진', '보크', '폭투', 'ERA', 'FIP', 'WHIP', 'ERA+', 'FIP+', 'WPA', 'WAR']
    
    # 컬럼만 있는 빈 데이터프레임 생성
    pitch_df = pd.DataFrame(columns=record_col)
    
    # 각 선수들의 기록을 행 형태로 삽입하기 위하여 Series 형태로 변환 뒤 df에 삽입
    for c in crawling_list:
        pitch_df = pitch_df.append(pd.Series(c, index=pitch_df.columns), ignore_index=True)
        
    # 시즌과 팀 이름 분리
    pitch_df['시즌'] = pitch_df.팀.str[:2]
    pitch_df['팀'] = pitch_df.팀.str[2:]
    
    return pitch_df