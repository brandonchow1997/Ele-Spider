def split_cookies(raw_cookie):
    # Chrome上直接复制下的cookie值
    raw_cookies = '{raw_cookie}'.format(raw_cookie=raw_cookie)
    # 申明键和值的列表
    keys = []
    values = []
    # 先根据;拆分各个cookie，得到cookie_list列表
    cookie_list = raw_cookies.split(";")
    # print(cookie_list)
    # len_list = len(cookie_list)
    # 再根据 = 拆分键和值
    for item in cookie_list:
        keys.append(item.split('=', 1)[0])
        values.append(item.split('=', 1)[1])
        # print(item.split('=', 1))
    # print(keys)
    # print(values)
    cookies = dict(zip(keys, values))
    # print(cookies)
    return cookies
