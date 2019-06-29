import os
import json
import numpy as np
import pandas as pd
from conf import settings


def save_json(username: str, content: dict):
    """保存json文件"""
    user_path = os.path.join(settings.DB_PATH, f'{username}.json')
    with open(user_path, 'w', encoding='utf8') as fw:
        json.dump(content, fw)


def read_json(username: str) -> dict:
    """读取json文件"""
    user_path = os.path.join(settings.DB_PATH, f'{username}.json')
    with open(user_path, 'r', encoding='utf8') as fr:
        data = json.load(fr)

    return data


def save_excel(df, filename):
    """保存excel"""
    df.to_excel(filename)


def read_excel(filename):
    """读取excel"""
    df = pd.read_excel(filename, index_col=0, header=0)

    return df


if __name__ == '__main__':
    save_json('nick', {'name': 'nick'})
    data = read_json('nick')
    print(data)

    arr = np.random.rand(3, 4)
    df = pd.DataFrame(arr)
    save_excel(df)
    data = read_excel(settings.GOODS_INFO_PATH)
    print(data)
