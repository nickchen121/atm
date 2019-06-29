# # # import numpy as np
# # # # import pandas as pd
# # # #
# # # # arr = np.random.rand(3, 4)
# # # # print(arr)
# # # # df = pd.DataFrame(arr)
# # # # print(df)
# # # # # save_excel(df)
# # # # # data = read_excel()
# # # # # print(data)
# # # # from conf import settings
# # # # import os
# # # #
# # # # with open(os.path.join(settings.LOG_PATH,'log.log'), 'r', encoding='utf8') as fr:
# # # #     s = ''
# # # #     for i in fr:
# # # #         if i.split('[')[-1].startswith('nick'):
# # # #             s += i
# # # # print(s)
# from db import db_handler
# from conf import settings
# #
# df = db_handler.read_excel(settings.GOODS_INFO_PATH)
# print(df.loc['price', :].to_list())
# # print(df.iloc[1:2]['tesla'])
# # df.iloc[1:2]['tesla'] -= 5
# df.loc['amount','tesla'] -= 5
# # print(df.loc['price', 'tesla'])
# print(id(df))
# # #
# # # # dic  = {"username": "nick", "pwd": "202cb962ac59075b964b07152d234b70", "extra": 14990, "locked": 0}
# # # # shopping_car_dict = {'transformer': 100,'transformer1': 100}
# # # # print(dic.update(shopping_car_dict))
# # # # print(dic)
# # shopping_car_dict={'tesla':50,'tesla1':50}
# #
# # for key in shopping_car_dict.keys():
# #     shopping_car_dict.clear()
# # print(shopping_car_dict)

lis = [0,1,2,3]
for i in range(len(lis)):
    lis[i]-=0.5

print(lis)