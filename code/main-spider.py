import eleme_spider
import split_cookies

if __name__ == '__main__':
    # -----------获取代理IP
    # -----------
    geohash = 'wx4gd94yjny1'
    # ----位置参数--------
    latitude = '39.996794'
    longitude = '116.48105'

    # ----cookies---

    # 需要填cookie--
    raw_cookie = 'SID='
    # ------
    cookies = split_cookies.split_cookies(raw_cookie)
    # print(cookies)
    # --------------

    # -----爬取页面开始和结束
    # -----每页10个店铺信息
    start_page = 1
    end_page = 100
    # 主函数--------
    eleme_spider.main(geohash, latitude, longitude, start_page, end_page, cookies)
    # --------------
