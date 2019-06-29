from db import db_handler
from conf import settings
from lib import common

shopping_car_dict = dict()


def read_goods_interface():
    df = db_handler.read_excel(settings.GOODS_INFO_PATH)

    return df


df = read_goods_interface()


def shopping_interface():
    while True:
        print(df)
        common.goods_visualize(df)
        # 打印商品信息
        goods = df.columns
        goods_choice = input('请选择你需要的商品,输入q退出>>>').strip()

        if goods_choice == 'q':
            break

        if goods_choice in goods:
            count_choice = input('请输入你需要购买的商品数量,输入q退出>>>').strip()

            if count_choice == 'q':
                break

            count_choice = int(count_choice)

            if int(df.loc['amount', goods_choice]) < count_choice:
                print('傻逼,库存不足')
                continue
            else:
                goods_price = int(df.loc['price', goods_choice])
                if shopping_car_dict.get(goods_choice):
                    shopping_car_dict[goods_choice] += (count_choice * goods_price)
                else:
                    shopping_car_dict[goods_choice] = (count_choice * goods_price)
                print(f'已经把{goods_choice}*{count_choice}加入购物车')
                df.loc['amount', goods_choice] -= count_choice
        else:
            print('傻逼,中文看不懂,英文也看不懂')

    return f'已加入购物车{shopping_car_dict}'


def shopping_car_interface(shopping_car_dict, username):
    goods_price = sum(shopping_car_dict.values())
    username_data = db_handler.read_json(username)

    if username_data['extra'] >= goods_price:
        username_data['extra'] -= goods_price
        username_data.update(shopping_car_dict)
        db_handler.save_json(username, username_data)
        new_shopping_car_dict = shopping_car_dict.copy()
        shopping_car_dict.clear()

        # 保存为excel文件
        db_handler.save_excel(df, settings.GOODS_INFO_PATH)
        return True, f'购物成功{new_shopping_car_dict}'
    else:
        shopping_car_dict.clear()

        return False, '穷逼也购物'


if __name__ == '__main__':
    read_goods_interface()
