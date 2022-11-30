# -*- coding: utf-8 -*-

import urllib
import json
import random
import pandas as pd
from urllib import parse
from random import choices
import numpy as np
from urllib.request import Request, urlopen
from random import randrange
from bs4 import BeautifulSoup
from korean_name_generator import namer

users = []
household = [1] * 334 + [2] * 280 + [3] * 201 + [4] * 147 + [5] * 36

start_date = pd.to_datetime('1948-01-01')
end_date = pd.to_datetime('2002-12-31')
birth = (pd.date_range(start_date, end_date, freq = 'D'))

# male_count와 female_count를 설정해주세요.
male_names = []
male_count = 250
female_names = []
female_count = 250

while len(male_names) < male_count:
    name = namer.generate(True)
    if name not in male_names:
        male_names.append(name)

while len(female_names) < female_count:
    name = namer.generate(False)
    if name not in female_names:
        female_names.append(name)

# 한글이름을 영어로 번역할 주소
naver_url = 'https://dict.naver.com/name-to-roman/translation/?query='


def get_eng_name(name):
    """ 한글이름을 영어로 번역하는 함수 """
    name_url = naver_url + urllib.parse.quote(name)

    req = Request(name_url)
    res = urlopen(req)

    html = res.read().decode('utf-8')
    bs = BeautifulSoup(html, 'html.parser')
    # Beautiful Soup를 사용해 Selector로 영문 이름 획득
    name_tags = bs.select('#container > div > table > tbody > tr > td > a')
    names = [name_tag.text for name_tag in name_tags]

    if len(names) == 0:
        return 'user_id'

    return names[0]

if male_count > 0:
    for i, male_name in enumerate(male_names):
        male = {}
        male['id'] = i + 1
        male['name'] = male_name
        male['sex'] = 'M'
        # 10대 - 50대에 걸쳐 생성되도록 age 설정
        male['birth'] = str(birth[random.randint(1,19089)])[:10].replace('-','')
        try:
            male['user_id'] = get_eng_name(
                male_name).lower().replace(' ', '') + '{:04d}'.format(i + 1)
        except:
            male['user_id'] = 'user_id' + '{:04d}'.format(i + 1)
        male['password'] = get_eng_name(male_name).replace(' ','').lower() + str(random.randint(1,99))
        male['household'] = int(str(choices(household,k=1)).replace('[','').replace(']',''))
        users.append(male)

        print('현재 ' + str(i + 1) + ' 번째 진행중: ' + male['user_id'])

if female_count > 0:
    for i, female_name in enumerate(female_names):
        female = {}
        female['id'] = i + male_count + 1
        female['name'] = female_name
        female['sex'] = 'F'
        female['birth'] = str(birth[random.randint(1,19089)])[:10].replace('-','')
        try:
            female['user_id'] = get_eng_name(
                female_name).lower().replace(' ', '') + '{:04d}'.format(i + male_count + 1)
        except:
            female['user_id'] = 'user_id' + '{:04d}'.format(i + 1)
        female['password'] = get_eng_name(female_name).replace(' ','').lower() + str(random.randint(1,99))
        female['household'] = int(str(choices(household,k=1)).replace('[','').replace(']',''))
        users.append(female)

        print('현재 ' + str(i + male_count + 1) +
              ' 번째 진행중: ' + female['user_id'])

with open('user_data.json', 'w', encoding='UTF-8') as json_file:
    json.dump(users, json_file, ensure_ascii=False)