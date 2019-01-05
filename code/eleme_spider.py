# -*- coding： utf-8 -*-

import requests
import time
import random


# import get_proxy


def get_page(geohash, latitude, longitude, page, cookies):
    # 代理IP
    """
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    """
    # ---------------

    cookie = cookies

    url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash={g}&latitude={v1}' \
          '&limit=20&longitude={v2}&offset={i}&terminal=web'.format(g=geohash, v1=latitude, v2=longitude, i=page*20-20)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36',
        'Referer': 'https://www.ele.me/place/{g}?latitude={v1}&longitude={v2}'.format(v1=latitude, v2=longitude, g=geohash),
    }
    try:
        response = requests.get(url, headers=header, cookies=cookie)
        # print(response.status_code)
        s = requests.Session()
        r = s.get(url, headers=header, cookies=cookie)
        add_cookie = requests.utils.dict_from_cookiejar(r.cookies)
        # print(add_cookie)
        # print(response.text)
        return response.json(), add_cookie
    except Exception:
        print('请检查IP/是否弹出验证码')
        pass


# -------------------------------


def parse(html, latitude, longitude, geohash, cookies):
    items = html
    for item in items:
        id = item['id']
        name = item['name']
        phone = item['phone']
        rating = item['rating']
        rating_count = item['rating_count']
        recent_order_num = item['recent_order_num']
        address = item['address']
        # flavors = item['flavors']

        item_list, sale_list = get_popular(id, latitude, longitude, geohash, cookies)
        print(item_list)
        item1 = item_list[0]
        sale1 = sale_list[0]
        try:
            item2 = item_list[1]
            sale2 = sale_list[1]
        except Exception:
            item2 = '缺失'
            sale2 = '缺失'

        tmp_list = [name, phone, address, str(rating), str(rating_count),
                    str(recent_order_num), item1, str(sale1),
                    item2, str(sale2)]
        print(tmp_list)
        write_info(tmp_list)


# ---------------------------
def write_info(info):
    file = open('../data/info.txt', 'a', encoding='utf-8')
    file.write(','.join(info))
    file.write('\n')
    file.close()


# --------------------------获取热销商品----------

def get_popular(id, latitude, longitude, geohash, cookies):
    # -------
    # ----------------
    item_list = []
    sale_list = []
    url = 'https://www.ele.me/restapi/shopping/v2/menu?restaurant_id={id}&terminal=web'.format(id=id)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36',
        'Referer': 'https://www.ele.me/place/{g}?latitude={v1}&longitude={v2}'.format(v1=latitude, v2=longitude, g=geohash),
    }
    response = requests.get(url, headers=header, cookies=cookies)
    try:
        json_data = response.json()
        hot_items = json_data[0]['foods']
        for item in hot_items[:2]:
            title = item['name']
            sales = item['month_sales']
            item_list.append(title)
            sale_list.append(sales)
        # print(item_list, sale_list)
        return item_list, sale_list
    except Exception:
        item_list = ['缺失', '缺失']
        sale_list = ['缺失', '缺失']
        return item_list, sale_list


# -------------------------------------------

def main(geohash, latitude, longitude, start_page, end_page, cookies):
    file = open('../data/info.txt', 'a', encoding='utf-8')
    file.write(",".join(['店名', '联系电话', '地址', 'tag1', 'tag2', '评分', '评分人数', '近期订单数', '热门商品1', '销量1', '热门商品2', '销量2']))
    file.write('\n')
    file.close()
    for i in range(start_page, end_page):
        # proxy = get_proxy.proxy_pool()
        print('正在爬取第', i, '页')
        time.sleep(1)
        print('店名 | 联系电话 | 地址 | tag1 | tag2 | 评分 | 评分人数 | 近期订单数 | 热门商品1 | 销量1 | 热门商品2 | 销量2')
        # 添加代理IP
        html, add_cookie = get_page(geohash, latitude, longitude, i, cookies)
        cookies.update(add_cookie)
        # ------------ 解析数据 ---------------
        parse(html, latitude, longitude, geohash, cookies)

