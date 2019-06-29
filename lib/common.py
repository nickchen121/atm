import os
import hashlib
import logging
import logging.config
from conf import settings
from interface import store


def login_auth(func):
    from core import src
    def wrapper(*args, **kwargs):
        # 判断是否登陆
        if not src.user_auth.get('username'):
            src.login()
            res = func(*args, **kwargs)
            return res

        res = func(*args, **kwargs)
        return res

    return wrapper


def load_logging_config(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)

    return logger


def check_user(username):
    """注册接口"""
    username_filename = os.path.join(settings.DB_PATH, f'{username}.json')
    if os.path.exists(username_filename):
        return True


def input_username_pwd():
    username = input('请输入你的用户名>>>').strip()
    pwd = input('请输入你的密码>>>').strip()

    # 密码加密
    m = hashlib.md5()
    m.update(pwd.encode('utf8'))
    pwd = m.hexdigest()

    return username, pwd


def goods_visualize(df):
    """想写就写"""
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    font = FontProperties(fname='D:\msyh.ttc')

    goods_columns = df.columns.to_list()

    goods_price = df.loc['price', :].to_list()
    price_index = list(range(len(goods_price)))

    goods_amount = df.loc['amount', :].to_list()
    amount_index = list(range(len(goods_amount)))

    fig = plt.figure()

    ax1 = fig.add_subplot(121)
    ax1.bar(price_index, goods_price,color='yellow')
    ax1.set_title('价格表', fontproperties=font)
    plt.xticks(amount_index, goods_columns, fontproperties=font, rotation=45)
    for i in amount_index:
        plt.text(amount_index[i],goods_price[i],s=goods_price[i])

    ax2 = fig.add_subplot(122)
    ax2.bar(amount_index, goods_amount,color='green')
    ax2.set_title('数量表', fontproperties=font)
    plt.xticks(amount_index,goods_columns,fontproperties=font,rotation=45)
    for i in amount_index:
        plt.text(amount_index[i],goods_amount[i],s=goods_amount[i])

    plt.suptitle('商品信息表', fontproperties=font, fontsize=15, weight='bold')
    plt.show()


if __name__ == '__main__':
    # res = check_user('nick')
    # print(res)
    goods_visualize()
