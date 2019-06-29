from lib import common
from interface import user, bank, store

logger = common.load_logging_config('user')

user_auth = {'username': None}

username = user_auth['username']


@common.login_auth
def logout():
    username = None
    user_auth['username'] = None
    print(f"{username}已经注销")
    logger.info(f"{username}已经注销")


def login():
    print('欢迎来到登陆功能')
    global username

    count = 0
    while count < 3:
        login_username, pwd = common.input_username_pwd()

        flag, msg, level = user.login_interface(login_username, pwd)
        print(msg)
        if flag:
            user_auth['username'] = login_username
            username = login_username
            logger.info(f'{username}登录成功')
            break

        # 判断是否需要锁定
        if level in [2, 3]:
            user.locked_interface(login_username)
            print('你的账户已经被锁定了')
            break

        count += 1


def register():
    print('欢迎来到注册功能')

    count = 0
    while count < 3:
        username, pwd = common.input_username_pwd()

        flag, msg = user.register_interface(username, pwd)
        # 判断是否注册成功
        print(msg)
        if flag:
            logger.info(f'{username}注册成功')
            break

        count += 1


@common.login_auth
def check_extra():
    print('欢迎来到查看余额功能')

    extra = bank.check_extra_interface(username)

    print(f'你的余额为{extra}')
    logger.info(f'{username}查看余额,余额为{extra}')

    return extra


@common.login_auth
def transfer():
    print('欢迎来到转账功能')

    from_username = username
    to_username = input('请输入你需要转账的用户>>>')
    flag = common.check_user(to_username)
    if flag:
        money = int(input('请输入你需要转账的金额'))
        flag, msg = bank.transfer_interface(from_username, to_username, money)
        print(msg)
        if flag:
            logger.info(f'{from_username}向{to_username}转了{money}')
            print(f'{from_username}向{to_username}转了{money}')
    else:
        print('用户不存在')


@common.login_auth
def repay():
    print('欢迎来到还款功能')

    flag, msg = bank.repay_interface(username)
    print(msg)
    logger.info(f'{username}{msg}')


@common.login_auth
def withdraw():
    print('欢迎来到取款功能')

    money = int(input('取现多少钱>>>').strip())

    flag, msg = bank.withdraw_interface(username, money)
    print(msg)
    if flag:
        logger.info(f'{username}{msg}')
        return


@common.login_auth
def history():
    print('欢迎来到银行流水查看功能')

    s = bank.history_interface(username)
    print(f'流水为:\n{s}')
    logger.info(f'{username}查看了流水')


@common.login_auth
def shopping():
    print('欢迎来到购物功能')

    msg = store.shopping_interface()
    print(f'{username}{msg}')
    logger.info(f'{username}{msg}')


@common.login_auth
def shopping_car():
    print('欢迎来到购车车功能')

    shopping_car_dict = store.shopping_car_dict

    flag, msg = store.shopping_car_interface(shopping_car_dict, username)
    print(msg)
    if flag:
        logger.info(f'{username}土豪{msg}')


def run():
    FUNC_DICT = {
        '0': logout,
        '1': login,
        '2': register,
        '3': check_extra,
        '4': transfer,
        '5': repay,
        '6': withdraw,
        '7': history,
        '8': shopping,
        '9': shopping_car,
    }
    from conf.settings import FUNC_MSG
    """运行函数，进行功能选择"""

    while True:
        for k, v in FUNC_MSG.items():
            print(f'{k}：{v}')
        func_choice = input('请选择你需要的功能，按q退出').strip()

        # 退出判断
        if func_choice == 'q':
            break

        # 获取功能
        func = FUNC_DICT.get(func_choice)

        if not func:
            print('傻逼，功能不存在')
            continue

        func()


if __name__ == '__main__':
    run()
