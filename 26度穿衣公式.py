# -*- coding: utf-8 -*-

"""
表格出處: https://www.thenorthface.com.tw/Article/Detail/80965

衣物溫度1-3°C的單品大多是身上必須著用的單品，也就是所謂的衣褲類別，上身及下著等，
3°C以上的單品則多為可疊加的單品如外套、大衣等。
(取自 https://www.elle.com/tw/fashion/street-snap/g45774900/weather-styling-tips/)

"""
from random import randint

pants = ['長褲', '長裙', '連身裙']
t1 = ['長T恤']
t2 = ['襯衫', '高領上衣', '薄外套']
t3 = ['針織衫', '薄毛衣', '薄帽T', '衛生衣']
t4 = ['西裝外套', '毛帽', '圍巾', '厚毛衣', '手套']
t5 = ['風衣外套', '高領厚毛衣', '厚帽T', '保暖鞋']
t6 = ['發熱衣', '輕薄羽絨衣', '厚棉外套']
t7 = ['毛呢大衣']
t8 = ['羽絨外套', '羊毛外套', '皮草外套']

calculate = {1:t1, 2:t2, 3:t3, 4:t4, 5:t5, 6:t6, 7:t7, 8:t8,
             9:t8, 10:t8}

while True:
    minT = int(input('請輸入明日預測的最低氣溫: '))
    maxT = int(input('請輸入明日預測的最高氣溫: '))
    if maxT < minT:
        print()
        print('最高溫應該小於最低溫，請重新輸入！')
        print()
    else:
        break

minD = 26-minT
maxD = 26-maxT
count1 = maxD
count2 = minD

clothes = []
more = []

#穿褲子和T恤至少要差2度，所以太熱就不適用
if minD < 2:
    print()
    print('天氣炎熱，不適用此穿搭公式！')
    print()
else:
    #先穿褲子
    minD = minD - 1
    maxD = maxD - 1
    clothes.append( pants[randint( 0, len(pants)-1 )] )
    
    #先穿1到3度的單品，只要至少一件單品就好
    for i in range(3, 0 ,-1):
        if maxD >= i:
            x = calculate[i][randint(0, len(calculate[i])-1 )]
            clothes.append(x) 
            #扣掉溫差，已經有保暖措施，沒那麼冷了
            maxD = maxD - i
            minD = minD - i
            break
    
    #從最高溫開始，記錄至少要穿多少(單品可以多穿幾件，不排除)
    for i in range(count1, 0 ,-1):
        #因為每次出現過就會刪掉，需要確認列表中是否還有元素，如果是空列表就跳過
        if maxD >= i and maxD <= 10 and len(calculate[i]) > 0:
            x = calculate[i][randint(0, len(calculate[i])-1 )]
            clothes.append(x) 
            #單品最多重複2件應該就很夠了，不需要再重複
            calculate[i].remove(x)
            maxD = maxD - i
            minD = minD - i
        #溫差太大會超出calculate的範圍
        elif maxD > 10:
            x = calculate[10][randint(0, len(calculate[10])-1 )]
            clothes.append(x) 
            #外套可能不要重複比較好，有出現過就刪掉
            calculate[10].remove(x)
            maxD = maxD - 10
            minD = minD - 10
    
    #再看最低溫，如果冷的話可以多穿這些
    for i in range(count2, 0 ,-1):
        #一樣，跳過空列表
        if minD >= i and minD <= 10 and len(calculate[i]) > 0:
            x = calculate[i][randint(0, len(calculate[i])-1 )]
            more.append(x) 
            calculate[i].remove(x)
            maxD = maxD - i
            minD = minD - i
        #跟上面 maxD > 10 一樣的原因
        elif minD > 10:
            x = calculate[10][randint(0, len(calculate[10])-1 )]
            more.append(x) 
            calculate[10].remove(x)
            maxD = maxD - 10
            minD = minD - 10
    
    #印出穿搭結果
    print()
    print('明日的推薦穿搭是',clothes, end = '')
    #避免穿搭只有一件褲子
    if len(clothes) == 1:
        print(' 並且搭配短袖等清涼單品')
    else:
        print()
    #早晚溫差大時再印出來
    if len(more) > 0:
        print('早晚溫差大時，可以再追加',more)