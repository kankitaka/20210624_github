#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import time
import random

tip = ["4/4、6/6、8/8、10/10、12/12は毎年必ず同じ曜日になる",
"カンガルーの誕生日は適当",
"毎年3900人の子どもが新たにタバコを吸い始める",
"パフェの語源は「パーフェクト」",
"アポロ11号とファミコンの容量は同じ",
"Twitterの鳥の名前はLally",
"1万円札の福沢諭吉の年齢は59歳",
"アンパンマンの飛行速度は秒速7.9km",
"下剤と下痢止めを一緒に飲むと下痢になる",
"トウモロコシの粒の個数は必ず偶数",
"チゲ鍋のチゲは辛いという意味ではなく鍋という意味、つまり鍋鍋",
"世界一長い曲は演奏が終わるまでに639年かかる",
"ガリガリ君が当たる確率は2～4%",
"パソコンのマウスを動かした時の長さの単位は「ミッキー」",
"太平洋の海水よりも大西洋の海水の方がしょっぱい",
"鼻水は体の中で1日に1L作られている",
"キティちゃんの名前はハローキティではなく正しくは「キティ・ホワイト」",
"叶姉妹は本当の姉妹ではない",
"阿佐ヶ谷姉妹は本当の姉妹ではない",
"B'zは昔A'zという名前であった",
"カスタードクリームは拳銃の弾を受け止める",
"ニコチンは体内に入るとコチニンになる",
"アンデスメロンのアンデスは「安心です」の略",
"バナナという名前のブドウがある",
"ゆず胡椒にはコショウは入っていない",
"日本にタバスコを広めたのはアントニオ猪木",
"鉛筆1本で56kmの線を書くことができる",
"赤ちゃんが泣き止まないときは反町隆史の「POISON」を聴かせると泣き止む",
"ベトナム語で鳩は「チンポコ」",
"テレビに一番初めに映ったのはカタカナの「イ」である",
"全ての赤ちゃんが「ラ」の音で泣き始める",
"ホッキョクグマの体毛は透明である",
"モナリザには眉毛もまつ毛もない",
"Windowsでは「prn」というフォルダを作れない",
"ミスターサタンとクリリンは同い年",
"Googleで「askew」と検索すると傾く",
]

origin_hour = []
origin_minite = []
user_number = []
root = tk.Tk()
root.geometry("600x200")
lbl_1 = tk.Label(text='時間の入力')
lbl_1.place(x=10,y=30)
lbl_2 = tk.Label(text='(h)')
lbl_2.place(x=200,y=30)
lbl_3 = tk.Label(text='(m)')
lbl_3.place(x=370,y=30)

txt_1 = tk.Entry()
txt_1.place(x=80,y=30)
txt_2 = tk.Entry()
txt_2.place(x=250,y=30)

def get_number():
    hour = txt_1.get()
    minite = txt_2.get()
    
    origin_hour.append(hour)
    origin_minite.append(minite)
    
    number_hour = 3600*int(txt_1.get())
    number_minite = 60*int(txt_2.get())
    user_number.append(number_hour + number_minite)
    
    txt_1.delete(0,tk.END)
    txt_2.delete(0,tk.END)
    label_1 = tk.Label(text=number_hour)
    label_2 = tk.Label(text=number_minite)
    
    #label_1 = tk.Label(text=origin_hour)
    #label_2 = tk.Label(text=origin_minite)
    
    label_1.place(x=20,y=50)
    label_2.place(x=50,y=50)

def start_timer():
    compare_number = 0
    time_sta = time.time()
    
    for n in range(len(user_number)):
        time.sleep(int(user_number[n])-compare_number)
        compare_number = int(user_number[n])
        time_end = time.time()
        tim = time_end - time_sta
        elapsed_time = int(round(tim)) / 3600
        #print("経過時間：",elapsed_time,"(h)")
        print("経過時間:",origin_hour[n],"(h)",origin_minite[n],"(m)")
        print("TIP",random.choice(tip))




btn1 = tk.Button(text="OK",command = get_number)
btn1.place(x=485,y=26)    

btn2 = tk.Button(text="START",command = start_timer)
btn2.place(x=525,y=26)
   


tk.mainloop()

