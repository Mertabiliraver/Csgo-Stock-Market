from selenium import webdriver
from tkinter import *
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
import hashlib

def eklenti_(driver):
    
    driver.get("https://chrome.google.com/webstore/detail/shadowpay-trademanager/obhadkdgdffnnbdfpigjklinjhbkinfh?hl=en")
    input("\nManager Script İnstall And 'ENTER' PRESS.")


def kontrol_et(driver):
    
    driver.get("https://shadowpay.com/tr/sell")
    sleep(4)
    deger = 1
    deger2 = 1
    deger3 = 1
    item_list = list()
    item_list2 = list()
    xpt_düzenle = list()

    driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[1]/div[3]/div[1]/div/div/div[2]/ul/a[2]/li/a").click()
    sleep(4)
   
    while True:
        

        try:
            item_text = driver.find_element_by_xpath(f"//*[@id='__layout']/div/main/div/div[1]/div[3]/div[4]/div/div/div/div[2]/div/div/div[2]/div/div/table/tbody/tr[{deger}]/td[2]/div/div[2]/div").text
            item_tur = driver.find_element_by_xpath(f"//*[@id='__layout']/div/main/div/div[1]/div[3]/div[4]/div/div/div/div[2]/div/div/div[2]/div/div/table/tbody/tr[{deger2}]/td[2]/div/div[3]/span").text
            xpt = driver.find_element_by_xpath(f"//*[@id='__layout']/div/main/div/div[1]/div[3]/div[4]/div/div/div/div[2]/div/div/div[2]/div/div/table/tbody/tr[{deger3}]/td[3]/div/div/div/input")
                
            print(str(item_text))
            print(str(item_tur))
            item_list.append(str(item_text))
            item_list2.append(str(item_tur))
            xpt_düzenle.append(xpt)

            deger += 1
            deger2 += 1
            deger3 += 1
        
        except:
            print("Tarama işlemi tamamlandı.")
            print(str(item_list))
            print(str(item_list2))
            break

    
    return item_list,item_list2,xpt_düzenle


def fiyat_bak(driver,itemler,türler):
    
    driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[1]/div[3]/div[4]/div/div/div/div[1]/button").click()
    sleep(3)  
    driver.find_element_by_xpath("//*[@id='__layout']/div/header/div/div/nav/ul/li[1]/a/div[2]").click()
    sleep(6)
    
    # sağ sol yaptırdığımız ( dota - csgo ) yer
    driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[2]/div/div[1]/div[1]/div/div[2]/div[2]/a[2]").click()
    sleep(5)
    driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[2]/div/div[1]/div[1]/div/div[2]/div[2]/a[1]").click()
    sleep(4)
    #driver.find_element_by_xpath("//*[@id='select-sort']/div[1]").click()
    #sleep(4)
    
    min_fiyat = list()

    ind = 0 
    driver.find_element_by_xpath("//*[@id='select-sort']/div[2]/div[2]/label/span").click() # kategori
    sleep(1)
    driver.find_element_by_xpath("//*[@id='select-sort']/div[2]/div[1]/label/span").click()
    sleep(4)

    for item in türler:
        print("[Döngü Sayısı]",ind)
        if str(item) in "MW":
            
            mw = "Minimal Wear"
            search = str(f"{itemler[ind]} {mw}") 
            #driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div").click()
            driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(search)
            print(search)
            sleep(3)
            #driver.find_element_by_xpath("//*[@id='select-sort']/div[1]").click() # küçükten büyüğe 
            #sleep(3)                  
            try:    
               min_dlr = driver.find_element_by_class_name("marketplace-item__price").text
               
               min_dlr = str(min_dlr).replace(".",",")
               vs1 = min_dlr.split(",")[1][:2]
               vö1 = min_dlr.split(",")[0]
               min_dlr = vö1 + "." + vs1

               
               min_fiyat.append(min_dlr)
               print(f"Min fiyat: ['{min_fiyat}']")
               sleep(1)

            except:
                driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(Keys.CONTROL+"a")
        
                print("Bu kendi itemin.")
                ind += 1
                continue

        elif str(item) in "FT":
            ft = "Field-Tested"
            search = str(f"{itemler[ind]} {ft}")
            #driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div").click()
            driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(search)
            print(search)                   
            sleep(3)
            #driver.find_element_by_xpath("//*[@id='select-sort']/div[1]").click() # küçükten büyüğe                   
            #sleep(3)                  
            try:    
               min_dlr = driver.find_element_by_class_name("marketplace-item__price").text
               
               min_dlr = str(min_dlr).replace(".",",")
               vs1 = min_dlr.split(",")[1][:2]
               vö1 = min_dlr.split(",")[0]
               min_dlr = vö1 + "." + vs1

               
               min_fiyat.append(min_dlr)
               print(f"Min fiyat: ['{min_fiyat}']")
               sleep(1)

            except:
                driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(Keys.CONTROL+"a")
        
                print("Bu kendi itemin.")
                ind += 1
                continue


        elif str(item) in "BS":      
            bs = "Battle-Scarred"
            search = str(f"{itemler[ind]} {bs}")
            #driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div").click()
            driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(search)
            print(search)
            sleep(3)
            #driver.find_element_by_xpath("//*[@id='select-sort']/div[1]").click() # küçükten büyüğe                   
            #sleep(3)                  
            try:    
               min_dlr = driver.find_element_by_class_name("marketplace-item__price").text
               
               min_dlr = str(min_dlr).replace(".",",")
               vs1 = min_dlr.split(",")[1][:2]
               vö1 = min_dlr.split(",")[0]
               min_dlr = vö1 + "." + vs1


               min_fiyat.append(min_dlr)
               print(f"Min fiyat: ['{min_fiyat}']")
               sleep(1)

            except:
                driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(Keys.CONTROL+"a")
        
                print("Bu kendi itemin.")
                ind += 1
                continue


        elif str(item) in "WW":
            ww = "Well-Worn"
            search = str(f"{itemler[ind]} {ww}")
            #driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div").click()
            driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(search)
            print(search)
            sleep(3)
            #driver.find_element_by_xpath("//*[@id='select-sort']/div[1]").click() # küçükten büyüğe                   
            #sleep(3)                  
            try:    
               min_dlr = driver.find_element_by_class_name("marketplace-item__price").text
               
               min_dlr = str(min_dlr).replace(".",",")
               vs1 = min_dlr.split(",")[1][:2]
               vö1 = min_dlr.split(",")[0]
               min_dlr = vö1 + "." + vs1

               
               min_fiyat.append(min_dlr)
               print(f"Min fiyat: ['{min_fiyat}']")
               sleep(1)

            except:
                driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(Keys.CONTROL+"a")
        
                print("Bu kendi itemin.")
                ind += 1
                continue


        elif str(item) in "FN":
            fn = "Factory New"
            search = str(f"{itemler[ind]} {fn}")
            #driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div").click()
            driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(search)
            print(search)
            sleep(3)
            #driver.find_element_by_xpath("//*[@id='select-sort']/div[1]").click() # küçükten büyüğe                   
            #sleep(3)                  
            try:    
               min_dlr = driver.find_element_by_class_name("marketplace-item__price").text
               
               min_dlr = str(min_dlr).replace(".",",")
               vs1 = min_dlr.split(",")[1][:2]
               vö1 = min_dlr.split(",")[0]
               min_dlr = vö1 + "." + vs1


               min_fiyat.append(min_dlr)
               print(f"Min fiyat: ['{min_fiyat}']")
               sleep(1)

            except:
                driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(Keys.CONTROL+"a")
        
                print("Bu kendi itemin.")
                ind += 1
                continue

        else:
            
            print("Bir sorun oluştu.")
            ind += 1
            continue
        
        driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input").send_keys(Keys.CONTROL+"a")
        sleep(5)
        
        ind += 1
    
    print(min_fiyat)
    return min_fiyat

def go_site(driver):
    driver.get("https://steamcommunity.com/openid/login?openid.ns=http://specs.openid.net/auth/2.0&openid.mode=checkid_setup&openid.return_to=https://thelogins.com/login/login/&openid.realm=https://thelogins.com/login&openid.ns.sreg=http://openid.net/extensions/sreg/1.1&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.identity=http://specs.openid.net/auth/2.0/identifier_select")
    input("login in and 'ENTER' PRESS.")
    driver.maximize_window()
    input("Manager script on and 'ENTER' PRESS.")
   




def fiyat_düzenle(driver,fiyatlar):
    driver.get("https://shadowpay.com/tr/sell")
    sleep(4)
    
    driver.find_element_by_xpath("//*[@id='__layout']/div/main/div/div[1]/div[3]/div[1]/div/div/div[2]/ul/a[2]/li/a").click()
    deger = 1
    indx = 0
    degercik = 0
    
    while True: 
        if indx == len(fiyatlar):
            print("Güncelleme işlemi tamamlandı.")
            break
        else:
            update = f"//*[@id='__layout']/div/main/div/div[1]/div[3]/div[4]/div/div/div/div[2]/div/div/div[2]/div/div/table/tbody/tr[{deger}]/td[3]/div/div/div/input"
            update2 = f"sell-list-items__button"

            index_fiyat = fiyatlar[indx]
            index_fiyat = index_fiyat.replace("[" , "").replace("]" , "").replace("'" , "").replace(" ","").replace("$","")
            index_fiyat = float(index_fiyat)
            index_fiyat -= 0.1
            
            
            index_fiyat = str(index_fiyat).replace(".",",")
            vsonrası = index_fiyat.split(",")[1][:2]
            vöncesi = index_fiyat.split(",")[0]
            index_fiyat = vöncesi + "," + vsonrası

            sleep(5)
            print("Güncellenmiş hali :",index_fiyat)
            driver.find_element_by_xpath(str(update)).send_keys(Keys.CONTROL+"a")
            driver.find_element_by_xpath(str(update)).send_keys(str(index_fiyat))
            sleep(2)

            driver.find_elements_by_class_name(str(update2))[degercik].click()
            sleep(3)
            deger += 1
            indx += 1







def gui_main():
    def sonsuz_sefer():
        lisans = ent1.get()
        
        
        
        
       
       
        if str(lisans) == "isikicinpil07":
            print("""
            Programın gerçek yapımcısı bilgileri...
            Mertcan Balcı'dır ve onun haricinde hiç bir yerden bu programı satın almayınız.
            İletişim: mertcanblc07@gmail.com

            NOT: Onun onaylamadığı bir bilgisayar programı çalıştırırsa kodlar otomatikman silinip bozulacaktır.

            """)
            sleep(5)
        
            driver = webdriver.Chrome()
            eklenti_(driver)
            go_site(driver)
            while True:

                itm,tür,tikla_düzelt = kontrol_et(driver)
                deger = fiyat_bak(driver,itm,tür)
                fiyat_düzenle(driver,deger)
                sleep(300)
        else:
            quit("Lisans şifresini doğru girip kullanınız.")





    def tek_sefer():
        lisans = ent1.get()
        
        
        
        
       
       
        if str(lisans) == "isikicinpil07":
            print("""
            Programın gerçek yapımcısı bilgileri...
            Mertcan Balcı'dır ve onun haricinde hiç bir yerden bu programı satın almayınız.
            İletişim: mertcanblc07@gmail.com

            NOT: Onun onaylamadığı bir bilgisayar programı çalıştırırsa kodlar otomatikman silinip bozulacaktır.

            """)
            sleep(5)
        
            driver = webdriver.Chrome()
            eklenti_(driver)
            go_site(driver)
            itm,tür,tikla_düzelt = kontrol_et(driver)
            deger = fiyat_bak(driver,itm,tür)
            fiyat_düzenle(driver,deger)
        else:
            quit("Lisans şifresini doğru girip kullanınız.")

    window = Tk()
    window.config(bg="black")
    window.resizable(0, 0)
    window.geometry("350x200")
    window.title("Exchange Bot")

    lbl1 = Label(text="Lisans Key:",bg="black",fg="white",font=("Calibri",14))
    lbl1.place(x=2,y=5)

    ent1 = Entry(font=("Calibri",14))
    ent1.place(x=100,y=7)
    
    btn1 = Button(text="Aralıklı sonsuz döngü.\n300 saniyede bir.",bg="green",fg="white",command=sonsuz_sefer,font=("Calibri",13))
    btn1.place(x=7,y=60)

    btn2 = Button(text="Tek seferlik döngü.\nKontrol eder ve durur.",bg="green",fg="white",command=tek_sefer,font=("Calibri",13))
    btn2.place(x=178,y=60)

    


    window.mainloop()




gui_main()

"""if str(data) == "mbe11112020":
    driver = webdriver.Chrome()
    eklenti_(driver)
    go_site(driver)
    itm,tür,tikla_düzelt = kontrol_et(driver)
    deger = fiyat_bak(driver,itm,tür)
    fiyat_düzenle(driver,deger)
else:
    quit("Programa şifresini doğru giriniz !")
    
"""
