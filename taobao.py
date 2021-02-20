from selenium import webdriver
import time
import datetime
browser = webdriver.Chrome()
state = 0

#設定時間: 小時:分鐘:秒.(六位小數)
settime = ("23:05:30.123456")
print("已設定時間:" + settime)

#登入後 勾選商品
browser.get("https://cart.taobao.com/cart.htm")
print("請勾選商品")
time.sleep(5)

while state == 0:
    #設定時間
    now = datetime.datetime.now().strftime('%H:%M:%S.%f') #設定時間
    print("現在時間" + now)

    #比較時間
    if (now > settime) and (state == 0) :
        print("時間到!!!!!!!!!!!!!!!!!!!!!!!!!")

        while state == 0 :
            print("嘗試按下結算")
            if browser.find_element_by_id("J_Go") :
                browser.find_element_by_id("J_Go").click()
                print("成功按下結算")
                state = 1
                break
            time.sleep(0.01)

        while state == 1 :
            print("嘗試按下提交訂單")
            if browser.find_element_by_link_text('提交订单') :
                browser.find_element_by_link_text('提交订单').click()
                print("跳轉到支付寶頁面")
            #檢測網址是否已經轉到alipay
            url = browser.current_url 
            if "alipay" in url : 
                print ("搶到了啦趕快付款")
                state = 2
                break
            else: 
                print ("似乎還沒搶到")
                time.sleep(0.01)

        time.sleep(0.01)

    time.sleep(0.01)

print("小聲bb一下 我真的不懂為什麼連裙子都要搞飢餓行銷")