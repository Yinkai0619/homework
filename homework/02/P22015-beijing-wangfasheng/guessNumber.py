# -*- coding: utf-8 -*-
# @file   : guessNumber.py
# @author : wfs
# @date   : 2019/06/04
# @version: 1.0
# @desc   : 猜数字功能

"""
功能描述：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或小了，直到用户猜中。
"""

# 导入模块
import random
# 随机生成一个三位以内的数字
answer = random.randint(1, 100)
# 请用户输入

while True:
    guess = int(input("请输入你猜的数字："))
    if guess == answer:
        print("恭喜你，猜对了！！！")
        break
    elif guess > answer:
        print("猜的数字大了！")
    else:
        print("猜的数字小了！")

# 写的没有啥问题
