# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import datetime
import sys

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}


def get_city(city):
    html = requests.get('https://' + city + '.fang.lianjia.com/loupan/', headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    where = soup.select('.resblock-have-find span')[2].text
    return where


def get_all_fang_url(city):
    url_list = []
    for page in range(1, 5):
        url = 'https://' + city + '.fang.lianjia.com/loupan/pg/' + str(page)
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        names = soup.select('a.name')
        for name in names:
            url_list.append(name['href'])
    return url_list


# 解码 unicode文本
def decode(string):
    return string


def strip(soup_obj):
    return decode(soup_obj.text).replace(' ', '').replace('\n', '')


def get_fang_info(url):
    url = 'https://' + city + '.fang.lianjia.com' + url
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')
    average_price = soup.select('.junjia')[0].text if len(soup.select('.junjia')) > 0 else '暂定'  # 均价
    house_list = soup.select('.p1')  # 户型介绍
    areas = []  # 面积
    orientations = []  # 朝向

    if len(house_list) > 0:
        for house in house_list:
            spans = house.select('span')
            areas.append(strip(spans[0]))
            orientations.append(strip(spans[1]))
    areas = list(set(areas))  # 去重
    orientations = list(set(orientations))

    price_list = soup.select('.p2')  # 房价
    fang_price = []
    if len(price_list) > 0:
        for price in price_list:
            if len(price.select('span')) > 0:
                fang_price.append(int(price.select('span')[0].text))
    fang_price = list(set(fang_price))

    details = soup.select('.label-val')  # 楼盘详情

    property_type = strip(details[5])  # 物业类型
    property_time = strip(details[8])  # 产权期限
    households = strip(details[10])  # 规划住户
    property_fee = strip(details[11])  # 物业费用

    floor_area = strip(details[18])  # 占地面积
    building_area = strip(details[19])  # 建筑面积

    fang = {'average_price': average_price,  # 均价  : 123
            'areas': areas,  # 面积  :[1,2,...]
            'orientations': orientations,  # 朝向  :[(东南),(西南),..]
            'fang_price': fang_price,  # 房价  :[126,135,..]
            'property_type': property_type,  # 物业类型 : 别墅，住宅..
            'property_time': property_time,  # 产权期限 : 70年
            'households': households,  # 规划住户 :1354
            'property_fee': property_fee,  # 物业费用 :4532元/月
            'floor_area': floor_area,  # 占地面积 :1663
            'building_area': building_area  # 建筑面积 :1023
            }
    fang_json['fangs'].append(fang)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    city = sys.argv[1]
    fang_json = {'fangs': []}
    url_list = get_all_fang_url(city)
    for url in url_list:
        get_fang_info(url)

    with open('fagns.json', 'w') as f:
        city_name = get_city(city)
        fang_json['city'] = city_name[1: 3]
        json.dump(fang_json, f)
        end_time = datetime.datetime.now()
        print(end_time - start_time)
