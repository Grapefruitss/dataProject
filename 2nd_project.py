import streamlit as st
import pandas as pd
import time


st.title(':two: 번째 프로젝트 :smile:')
# st.header('')
st.subheader('대한민국 의사증원, 몇 명이 적절한가 :grey_question')

with st.spinner( text = '로딩중... '):
    time.sleep(3.0)

col01,col02,col03 = st.tabs([':large_yellow_square: 데이터 분석', ':large_orange_square: 데이터 시각화', ':large_green_square: 프로젝트 결과'])

col01.write('세계 속 대한민국')
col01.image('oecd_doctor_wage.png')
print('\n')
col01.image('oecd_doctor_wage2.png')
print('\n')
col01.image('oecd_doc_num.png')

print('\n')

col01.write('고령화 속 대한민국')
col01.image('kr_older_expect_stat.png')
print('\n')
col01.image('oecd_older_rate1.png')
print('\n')
col01.image('oecd_older_rate2.png')

col02.write('한국')
col02.image('kr_doc_count.png')
col02.write('비율')
col02.image('ratio_of_doc.png')

col03.write('감사합니다 ')

st.sidebar.title(':black[공공데이터를 이용한 AI 챗봇 과정]')
st.sidebar.write('조장 : 김한솔')
st.sidebar.write('조원 : 이혁빈, 류동오, 황성현')
st.sidebar.write('')
st.sidebar.write('역할분담')
st.sidebar.write('김한솔 : 데이터수집·정리·시각화, 앱 개발 및 배포, 사전 및 중간 발표')
st.sidebar.write('이혁빈 : 데이터수집·정리·시각화')
st.sidebar.write('류동오 : 데이터 수집·정리')
st.sidebar.write('황성현 : 데이터 수집·정리, 최종 발표')
