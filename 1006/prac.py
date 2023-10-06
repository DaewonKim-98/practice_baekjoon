from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
plt.switch_backend('Agg')


csv_path = 'austin_weather.csv'
# Create your views here.

df = pd.read_csv(csv_path)

# x = ['No Events', 'Rain', 'Thunderstrom Events', 'Fog', 'Snow']
# y = 

# 기상 현상을 나타내는 딕셔너리
dic = {}

for k, v in df['Events'].value_counts().items():
    for i in k.split(' , '):
        # 만약 빈 값이면 그게 결측값이고 딕셔너리는 No Events의 키로 돼야하므로
        if i == ' ':
            dic['No Events'] = v
        # 딕셔너리에 기상현상이 있으면 그 값만 더하기
        elif i in dic:
            dic[i] += v
        # 딕셔너리에 기상현상이 없으면 딕셔너리 추가
        else:
            dic[i] = v

