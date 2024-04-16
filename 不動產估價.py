# -*- coding: utf-8 -*-

"""
租金：
每坪租金*100/100*（94年1月，案例的租金PI）/（比較的租金PI）*
        100/(100+所在地區修正率，好就往上修)*
        (100+個別條件修正率，差就往上修+樓層效用修正，看跟勘估差多少）/100

調整率最小的有最高權重，依序是40%、35%、25%，加權得出案例的市場每坪租金

有效總收入：
取min(契約租金, 市場客觀租金)
總收入記得要加入押金的本息，以年為單位
有效總收入 = 總收入*(1-空置率)，畢竟空著就沒有租金收入

總費用：
管理費還是用總收入計算，而非有效總收入
重建成本的20%，是主要設備費用的更換經費，/10以折到10年
整個重建成本(*總坪數)要/50以折到50年

有效總收入 - 總費用 = 淨收益

價格推估 = 比較標的價格 * (案例出租當時的價格指數)/(案例購買時的價格指數)*
          100/(價格調整，比如買價跟出租處的價格並不相同等)
          
勘估標的資本化率 = average(比較的資本化率)

"""

from statistics import mean
#租金指數、區域調整、個別調整、樓層調整、價格指數（買賣時）、價格指數（出租時）
rent_pi = []
region_fix = []
individual_fix = []
floor_fix = []
buy_pi_b = []
buy_pi_r = []
#每坪租金、總坪數
rent_by_p = []
total_p = []
#管理費%數、重建費用、設備折舊、設備年限、建築年限、標的買賣價格
manage = []
rebuilt = []
dep_equip = []
year_equip = []
year_build = []
buy_build = []
#'地價','地價稅率','房屋現值','房屋稅率',押金月數,'保險費率'
price_land = []
tax_land = []
price_house = []
tax_house = []
deposit_month = []
insurance = []


compare_data = [rent_pi, region_fix, individual_fix, floor_fix,
                buy_pi_b, buy_pi_r, rent_by_p, total_p, manage, 
                rebuilt, dep_equip, year_equip, year_build, buy_build]
compare_intro = ['租金指數','區域調整','個別調整', '樓層效用',
                 '價格指數(買賣時)', '價格指數(出租時)','每坪租金','總坪數','管理費%數',
                 '每坪重建費用','更換費用%數','設備年限','建築年限','標的買賣價格']
compare_data2 = [price_land, tax_land, price_house, tax_house, deposit_month, insurance]
compare_intro2 = ['地價','地價稅率','房屋現值','房屋稅率','押金月數','保險費率']

#勘估的各種變數，包含：
#(租金指數、樓層效用、契約每坪租金、總坪數、管理費%數、重建費用)
#(設備折舊、設備年限、建築年限、價格指數)
name = ['r_pi', 'f_f', 'r_by_p', 't_p', 'ma', 'rb', 'dep_e', 'dep_e_y', 
        'dep_b_y']
name2 = ['price_l', 'tax_l', 'price_h', 'tax_h', 'deposit_m', 'insur']
var = {'r_pi':0, 'f_f':0, 'r_by_p':0, 't_p':0, 'ma':0, 'rb':0,
        'dep_e':0, 'dep_e_y':0, 'dep_b_y':0}
var2 = {'price_l':0, 'tax_l':0, 'price_h':0, 'tax_h':0,
        'deposit_m':0, 'insur':0}
introduce = ['租金指數', '樓層效用', '契約每坪租金', '總坪數', '管理費%數', 
             '每坪重建費用', '更換費用%數', '設備年限', '建築年限']
intro2 = ['地價','地價稅率','房屋現值','房屋稅率','押金月數', '保險費率']

print('\033[0m因為會使用到的數字眾多，建議先用表格整理好',
      '可參考 https://reurl.cc/XqO4rE ', sep = '\n')
while True:
    check = input('準備好後，請按y開始輸入: ')
    if check == 'y':
        break

#輸入勘估標的
while True:
    print('\033[31m為了正確估價，請先告知勘估標的之各項數值')
    #輸入所有數值
    i = 0
    while i < len(introduce):
        try:
            x = float(input('\033[0m請輸入 %s: '%introduce[i]))
            var[name[i]] = x
            i += 1
        except ValueError:
            print('\033[31m格式錯誤，請重新輸入！')
            continue
    #輸入第二部分
    i = 0
    while i < len(intro2):
        try:
            x,y = map(float, input('\033[0m請輸入「%s」和「%s」(用空白隔開):'
                            %(intro2[i],intro2[i+1])).split(' '))
            var2[name2[i]] = x
            var2[name2[i+1]] = y
            i += 2
        except ValueError:
            print('\033[31m格式錯誤，請重新輸入！')
            continue
    #印出名稱和數值，確認是否正確
    print()
    j = 0
    for i in range(len(introduce)):
        j += 1
        print(f"{introduce[i]}：{var[name[i]]:,.0f}", end='\t')
        if j%2 == 0:
            print()
    j = 0
    for i in range(len(intro2)):
        j += 1
        if i % 2 == 0: 
            print(f"{intro2[i]}：{var2[name2[i]]:,.0f}", end='\t')
        else:
            print(f"{intro2[i]}：{var2[name2[i]]:,.1f}", end='\t')
        if j%2 == 0:
            print()
    print()
    check = input('\033[31m若勘估標的之資訊正確，請輸入y: ')
    print()
    if check != 'y':
        print('發生錯誤，請重新輸入')
        print()
    else:
        break
    
    
k=0
#輸入比較標的
while True:
    print('\033[0m接下來，請輸入比較標的之相關資料（一次輸入一件）')
    print('\033[31m提醒1: 當條件較「差」時，區域調整為「負數」，因為在分母')
    print('提醒2: 當條件較「差」時，個別調整為「正數」，因為在分子')
    print('提醒3: 當不需要調整時，輸入0即可')
    print('提醒4: 輸入標的買賣價格時，請記得先減掉車位價格！！')
    #開始輸入所有變數
    i = 0
    while i < len(compare_data):
        try:
            x = float(input('\033[0m請輸入 %s: '%compare_intro[i]))
            compare_data[i].append(x)
            i += 1
        except ValueError:
            print('\033[31m格式錯誤，請重新輸入！')
            continue
    i = 0
    while i < len(compare_data2):
        try:
            x,y = map(float, 
                      input('\033[0m請輸入「%s」和「%s」(用空白隔開):'
                            %(compare_intro2[i],compare_intro2[i+1])
                            ).split(' ') )
            compare_data2[i].append(x)
            compare_data2[i+1].append(y)
            i += 2
        except ValueError:
            print('\033[31m格式錯誤，請重新輸入！')
            continue
    #印出名稱和數值，方便確認輸入
    print()
    for i in range(len(compare_data)):
        j += 1
        print(f"{compare_intro[i]}：{compare_data[i][k]:,.0f}", end='\t')
        if j%2 == 0:
            print()
    for i in range(len(compare_data2)):
        j += 1
        if i % 2 == 0: 
            print(f"{compare_intro2[i]}：{compare_data2[i][k]:,.0f}", end='\t')
        else:
            print(f"{compare_intro2[i]}：{compare_data2[i][k]:,.1f}", end='\t')
        if j%2 == 0:
            print()
    print()
    check = input('\033[31m若比較標的之資訊正確，請輸入y: ')
    if check != 'y':
        print('\033[0m發生錯誤，請重新輸入所有比較標的')
        #租金指數、區域調整、個別調整、樓層調整、價格指數（買賣時）、價格指數（出租時）
        rent_pi = []
        region_fix = []
        individual_fix = []
        floor_fix = []
        buy_pi_b = []
        buy_pi_r = []
        #每坪租金、總坪數
        rent_by_p = []
        total_p = []
        #管理費%數、重建費用、設備折舊、設備年限、建築年限
        manage = []
        rebuilt = []
        dep_equip = []
        year_equip = []
        year_build = []
        #'地價','地價稅率','房屋現值','房屋稅率','保險費率','每坪月押金'
        price_land = []
        tax_land = []
        price_house = []
        tax_land = []
        insurance_rate = []
        deposit_month = []
        k = 0
    else:
        check = input('若想繼續輸入其他比較標的，請輸入y，或按任意鍵結束輸入: ')
        print()
        if check != 'y':
            break
    k += 1

print()
print('\033[31m輸入完成！現在開始計算……')

#建立列表來儲存比較標的之市場租金、區域調整率、個別調整率、總調整率
rent_new = []
adj_reg = []
adj_ind = []
adj_total = []
i = 0
#計算調整租金
while True:
    print('\033[0m')
    print('\033[31m計算比較標的%d之調整後租金'%(i+1))
    adjust1 = var['r_pi']/rent_pi[i]
    print('\033[0m租金指數調整為 %d / %d = %.3f'%(var['r_pi'], rent_pi[i], adjust1))
    print('## 租金指數調整=勘估之租金指數/比較之租金指數 ##')
    adjust2 = 100/(100 + region_fix[i])
    print('區域調整為 100 / (100 + %d) = %.3f'%(region_fix[i], adjust2))
    print('## 區域調整=100/(100+區域調整率) ##')
    floor = var['f_f']-floor_fix[i]
    adjust3 = (100 + individual_fix[i] + floor)/100
    print('個別調整為 ( 100+%d+%d )/100 = %.3f'
          %(individual_fix[i], floor, adjust3))
    print('## 個別調整=(100+個別調整+與勘估樓層效用的差)/100 ##')
    adjust4 = adjust1*adjust2*adjust3
    print('總調整率 = %.3f * %.3f * %.3f = %.3f'
          %(adjust1, adjust2, adjust3, adjust4))
    new_rent = round( rent_by_p[i] * adjust4 )
    print('調整後市場租金為 %d * %.3f = %d'
          %(rent_by_p[i], adjust4, new_rent))
    check = input('\033[31m請輸入y以計算下一個比較標的之租金，或按任意鍵結束計算: ')
    rent_new.append(new_rent)
    adj_reg.append(round(adjust2 - 1,3))
    adj_ind.append(round(adjust3 - 1,3))
    adj_total.append(round(adjust4 - 1,3))
    i += 1
    if i == 3:
        break
    if check != 'y':
        check = input('真的要結束計算嗎？請再次輸入y: ')
        if check != 'y':
            continue
        break

#比較調整率，得出客觀租金
rent_market = 0
while True:
    print('\033[0m確認比較標的跟勘估標的，是否足夠相近')
    print()
    print('個別因素調整率依序為:',adj_ind)
    print('區域因素調整率依序為:',adj_reg)
    print('總調整率依序為',adj_total)
    Max = max(rent_new)
    Min = min(rent_new)
    dif = round( (Max-Min) / ( (Max+Min)/2 ) ,4)
    print('租金差異率為:',dif)
    adj_ab = []
    rank = []
    for i in range(len(adj_total)):
        adj_ab.append( abs(adj_total[i]) )
    
    #依總調整率是否相同，分成三種加權
    unique = len(set(adj_ab))
    
    if unique == 1:
        for i in range(len(adj_ab)):
            rank.append(1/3)
    elif unique == 3:
        for i in range(len(adj_ab)):
            if adj_ab[i] == min(adj_ab):
                rank.append(0.40)
            elif adj_ab[i] == max(adj_ab):
                rank.append(0.25)
            else:
                rank.append(0.35)
    else:
        if adj_ab.count(max(adj_ab)) == 2:
            for i in range(len(adj_ab)):
                if adj_ab[i] == min(adj_ab):
                    rank.append(0.40)
                else:
                    rank.append(0.30)
        else:
            for i in range(len(adj_ab)):
                if adj_ab[i] == max(adj_ab):
                    rank.append(0.30)
                else:
                    rank.append(0.35)

    weight = []
    for i in range(len(rent_new)):
        weight.append(rent_new[i]*rank[i])
    
    #計算加權客觀租金
    print('客觀租金為: ')
    print('%d * %.2f + %d * %.2f + %d * %.2f = %d'
          %(rent_new[0], rank[0], rent_new[1], rank[1],
            rent_new[2], rank[2], round( sum(weight) ) ))
    rent_market = int(sum(weight)/10)*10
    print('去零頭，取客觀租金為: %d'%rent_market)
    break
    
#計算勘估標的之淨收益
interest = empty = net = 0
while True:
    #取契約租金和客觀租金中，最小的那個
    rent = 0
    if var['r_by_p'] <= rent_market:
        print('契約租金小於客觀租金，故使用契約租金 %d'%var['r_by_p'])
        rent = var['r_by_p']
    else:
        print('契約租金大於客觀租金，故使用客觀租金 %d'%rent_market)
        rent = rent_market
    
    print()
    #計算有效總收入
    interest = float(input('請輸入一年期定期存款利率%數: '))
    empty = float(input('請輸入空置率%數: '))
    revenue_rent = rent * var['t_p'] * 12
    print(f"租金收入: {rent:,.0f} * {var['t_p']} * 12 = {revenue_rent:,.0f}")
    print('(租金收入=每坪月租金*總坪數*一年有12個月)')
    revenue_deposit = rent*var['t_p']*var2['deposit_m']*interest/100
    print(f"押金孳息收入: {rent:,.0f} * {var['t_p']} * {var2['deposit_m']} * {interest/100:.2f} = {revenue_deposit:,.0f}")
    print('(押金孳息收入=每坪月租金*總坪數*押金月數*一年期定存利率)')
    revenue_total = round( revenue_rent + revenue_deposit )
    print(f"總收入= 租金收入({revenue_rent:,.0f}) + 押金孳息收入({revenue_deposit:,.0f}) = {revenue_total:,.0f}")
    eff_revenue = round(revenue_total * (100 - empty)/100)
    print(f"\033[31m有效總收入 = 總收入 * (1-空置率) = {revenue_total:,.0f} * (1-{empty/100:.2f}) = {eff_revenue:,.0f}")
    print('\033[0m')
    
    #計算總費用
    spend1 = round(var2['price_l'] * var2['tax_l'] / 100)
    print(f"地價稅額 = 土地現價({var2['price_l']:,.0f}) * 地價稅率({var2['tax_l']/100:.3f}) = {spend1:,.0f}")
    spend2 = round(var2['price_h'] * var2['tax_h'] / 100)
    print(f"房屋稅 = 房屋現價({var2['price_h']:,.0f}) * 房屋稅率({var2['tax_h']/100:.3f}) = {spend2:,.0f}")
    spend3 = round(var2['price_h'] * var2['insur'] / 100)
    print(f"保險費 = 房屋現價({var2['price_h']:,.0f}) * 保險費率({var2['insur']/100:.3f}) = {spend3:,.0f}")
    spend4 = round(revenue_total * var['ma'] / 100)
    print(f"管理維護費 = 總收入({revenue_total:,.0f}) * 管理費率({var['ma']/100:.2f}) = {spend4:,.0f}")
    spend5 = round(var['rb'] * var['t_p'] * var['dep_e'] / 100 / var['dep_e_y'])
    print(f"重置提撥費 = 每坪重置費({var['rb']:,.0f}) * 總坪數({var['t_p']}) * 更換費({var['dep_e']/100:.2f}) / 年數({var['dep_e_y']}) = {spend5:,.0f}")
    spend6 = round(var['rb'] * var['t_p'] / var['dep_b_y'])
    print(f"折舊提存費 = 每坪重置費({var['rb']:,.0f}) * 總坪數({var['t_p']}) / 建築年數({var['dep_b_y']}) = {spend6:,.0f}")

    
    #全部加總
    print()
    sp_total = spend1 + spend2 + spend3 + spend4 + spend5 + spend6
    print(f"\033[31m費用合計: {sp_total:,.0f}")
    print('')
    
    #計算淨收益
    net = eff_revenue - sp_total
    print(f"\033[31m淨收益 = 有效總收入({eff_revenue:,.0f}) - 總費用({sp_total:,.0f}) = {net:,.0f}")
    print('\033[0m')
    break

check = ''
while check != 'y':
    check = input('請按y以開始計算比較標的之淨收益: ')

#計算比較標的之淨收益、價格推估、收益資本化率
capital_rate = []
for count in range(3):
    #計算有效總收入
    revenue_rent = rent_by_p[count] * total_p[count] * 12
    print(f"租金收入: {rent_by_p[count]:,.0f} * {total_p[count]} * 12 = {revenue_rent:,.0f}")
    print('(租金收入=每坪月租金*總坪數*一年有12個月)')
    revenue_deposit = rent_by_p[count] * total_p[count] * deposit_month[count] * interest/100
    print(f"押金孳息收入: {rent_by_p[count]:,.0f} * {total_p[count]} * {deposit_month[count]} * {interest/100:.2f} = {revenue_deposit:,.0f}")
    print('(押金孳息收入=每坪月租金*總坪數*押金月數*一年期定存利率)')
    revenue_total = round( revenue_rent + revenue_deposit )
    print(f"總收入= 租金收入({revenue_rent:,.0f}) + 押金孳息收入({revenue_deposit:,.0f}) = {revenue_total:,.0f}")
    eff_revenue = round(revenue_total * (100 - empty)/100)
    print(f"\033[31m有效總收入 = 總收入 * (1-空置率) = {revenue_total:,.0f} * (1-{empty/100:.2f}) = {eff_revenue:,.0f}")
    print('\033[0m')
    
    #計算總費用
    spend1 = round(price_land[count]* tax_land[count] / 100)
    print(f"地價稅額 = 土地現價({price_land[count]:,.0f}) * 地價稅率({tax_land[count]/100:.3f}) = {spend1:,.0f}")
    spend2 = round(price_house[count] * tax_house[count] / 100)
    print(f"房屋稅 = 房屋現價({price_house[count]:,.0f}) * 房屋稅率({tax_house[count]/100:.3f}) = {spend2:,.0f}")
    spend3 = round(price_house[count] * insurance[count] / 100)
    print(f"保險費 = 房屋現價({price_house[count]:,.0f}) * 保險費率({insurance[count]/100:.3f}) = {spend3:,.0f}")
    spend4 = round(revenue_total * manage[count] / 100)
    print(f"管理維護費 = 總收入({revenue_total:,.0f}) * 管理費率({manage[count]/100:.2f}) = {spend4:,.0f}")
    spend5 = round(rebuilt[count] * total_p[count] * dep_equip[count] / 100 / year_equip[count])
    print(f"重置提撥費 = 每坪重置費({rebuilt[count]:,.0f}) * 總坪數({total_p[count]}) * 更換費({dep_equip[count]/100:.2f}) / 年數({year_equip[count]}) = {spend5:,.0f}")
    spend6 = round(rebuilt[count] * total_p[count] / year_build[count])
    print(f"折舊提存費 = 每坪重置費({rebuilt[count]:,.0f}) * 總坪數({total_p[count]}) / 建築年數({year_build[count]}) = {spend6:,.0f}")
    
    #全部加總
    print()
    sp_total = spend1 + spend2 + spend3 + spend4 + spend5 + spend6
    print(f"\033[31m費用合計: {sp_total:,.0f}")
    print('')
    
    #計算淨收益
    net_com = eff_revenue - sp_total
    print(f"\033[31m淨收益 = 有效總收入({eff_revenue:,.0f}) - 總費用({sp_total:,.0f}) = {net_com:,.0f}")
    print('\033[0m')
    
    #計算價格推估
    x = eval(input('請輸入價格推估的特別調整\n（可以為算式，無請輸入1）: '))
    price = buy_build[count]*buy_pi_r[count]/buy_pi_b[count]*x
    print(f"\033[31m價格推估 = {buy_build[count]:,.0f} * {buy_pi_r[count]} / {buy_pi_b[count]} * {x:.3f}\n"
          f"= {price:,.0f}")
    print('\033[0m價格推估 = 比較標的價格 * (案例出租當時的價格指數)/(案例購買時的價格指數) * ',
          '(價格調整，ex. 買賣價格跟出租處的樓層並不同)', sep='')
    
    #計算收益資本化率，並存到list裡
    print()
    capital = round( net_com / price ,4) 
    print(f"收益資本化率 = 淨收益({net_com:,.0f}) / 標的價格推估({price:,.0f}) = {capital:,.4f}")
    capital_rate.append(capital)
    
    #確認是否繼續算
    print()
    check = input('按y繼續計算下一個比較標的: ')
    if check != 'y':
        check2 = input('確定要結束計算嗎？按y表示確認: ')
        if check2 == 'y':
            break
    print()

#計算平均資本化率
print()
print('收益資本化率依序為:',capital_rate)
ave = round( mean(capital_rate) ,3)
print('平均資本化率為: %.3f'%ave)

final = round( net / ave )
print(f"\033[31m勘估標的價格 = \n"
      f"    勘估標的淨收益({net:,.0f}) / 平均資本化率({ave:.3f}) = {final:,.0f}")
final_ping = round( final / var['t_p'] )
print(f"除以總坪數({var['t_p']})後，約合每坪 {final_ping:,.0f} 元")


