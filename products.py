# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:09:33 2021

@author: Win10
"""

products = []
while True:
    name = input('請輸入商品名稱 :')
    if name == 'q':
        break
    price = input('請輸入商品價格 :')
   # p = []
   # p.append(name)
   # p.append(price)
    products.append([name, price])
print(products)

for product in products:
     print('商品的名稱是', product[0],'商品的價格是', product[1], '元')
     