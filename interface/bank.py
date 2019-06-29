import os
from conf import settings
from db import db_handler


def check_extra_interface(username):
    """检查余额接口"""
    data = db_handler.read_json(username)
    return data['extra']


def transfer_interface(from_username, to_username, money):
    from_username_data = db_handler.read_json(from_username)
    to_username_data = db_handler.read_json(to_username)

    if from_username_data['extra'] > money:
        to_username_data['extra'] += money
        from_username_data['extra'] -= money

        db_handler.save_json(from_username, from_username_data)
        db_handler.save_json(to_username, to_username_data)

        return True, '转账成功'

    return False, '转账失败'


def repay_interface(username):
    username_data = db_handler.read_json(username)
    extra = username_data['extra']

    if extra >= 15000:
        return True, '无需还款'
    else:
        username_data['extra'] = 15000
        db_handler.save_json(username, username_data)
        return True, f'还款{(15000-extra)*1.005}成功'


def withdraw_interface(username, money):
    username_data = db_handler.read_json(username)
    if username_data['extra'] > money:
        username_data['extra'] -= money
        db_handler.save_json(username, username_data)
        return True, f'取现{money}成功'

    return False, f'余额不足'


def history_interface(username):
    filename = os.path.join(settings.LOG_PATH, 'log.log')
    with open(filename, 'r', encoding='utf8') as fr:
        s = ''
        for i in fr:
            if i.split('[')[-1].startswith(username):
                s += i
    return s
