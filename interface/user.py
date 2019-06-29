from lib import common
from db import db_handler


def register_interface(username, pwd):
    """注册接口"""
    flag = common.check_user(username)
    if flag:
        return False, '用户已经存在'
    else:
        content = {'username': username, 'pwd': pwd, 'extra': 15000, 'locked': 0}
        db_handler.save_json(username, content)
        return True, '用户注册成功'


def login_interface(username, pwd):
    # 判断用户是否存在
    flag = common.check_user(username)
    if not flag:
        return False, '用户不存在', 1

    # 判断用户是否锁定
    data = db_handler.read_json(username)
    if data['locked']:
        return False, '用户已经锁定，去解锁', 2

    # 判断密码
    if pwd == data['pwd']:
        return True, '登陆成功', 0

    return False, '密码错误', 3


def locked_interface(username):
    """输入密码错误就锁"""
    data = db_handler.read_json(username)
    data['locked'] = 1
    db_handler.save_json(username, data)
