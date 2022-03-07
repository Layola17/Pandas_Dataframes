#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

Chips =['Simba','Lays']
Cooldrinks = ['Coke','Fanta']
Chocolates = [' Cadbury', 'Tex']
Pies =['Pepper Steak', 'Chicken']
Fruit =['Pear', 'Apple', 'Orange']
Cupcakes =['vanilla', 'chocolate']
Veggies =['spinach', 'cabbage']

df = pd.DataFrame(list(zip(Chips,Cooldrinks,Chocolates,Pies,Fruit,Cupcakes,Veggies)),
                  columns=['Chips','Cooldrinks','Chocolates','Pies', 'Fruit', 'Cupcakes', 'Veggies'])
df

