#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
user_decide_time =[]
while(1):
    number = input('time-set >>>')
    if number.isdecimal():
        number = int(number) 
        break
user_decide_time.append(number)
time_sta = time.time()
time.sleep(user_decide_time[0])
print("かんきたかひろ")
time_end = time.time()
tim = time_end - time_sta
print(tim)


# In[ ]:




