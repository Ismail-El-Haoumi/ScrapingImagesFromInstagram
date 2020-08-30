from selenium import webdriver
from time import sleep
import os
from bs4 import BeautifulSoup
import requests
import shutil
import lxml



class App:
    def __init__(self,username='elhoumi.mks',password='allahoakbar2000',target_username='sarah.zain44',path="C:\\Users\\ismail\\Desktop\\python-test-torrent"):
        self.username=username
        self.password=password
        self.target_username=target_username
        os.makedirs(path+'\\'+target_username)
        self.path=path+'\\'+target_username
        self.driver=webdriver.Chrome("C:\\Users\\ismail\\Downloads\\chromedriver.exe")
        #self.driver = webdriver.PhantomJS("C:\\Users\\ismail\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

        self.main_url='https://www.instagram.com'
        self.driver.get(self.main_url)
        sleep(2)
        self.log_in()
        sleep(2)
        self.open_target_profile()
        sleep(2)
        self.list=[]
        self.scrroll_down()
        sleep(5)
       # self.downloading_images()
        #input("stop for now")
        sleep(3)
        self.driver.close()

    def downloading_images(self,iii):
        soup=BeautifulSoup(self.driver.page_source,"lxml")
        all_images=soup.find_all('img')
        hh=self.driver.find_elements_by_class_name("FFVAD")
        print(len(hh))
        print('length of all images',len(all_images))
        for image in all_images:

            filename='image_'+str(self.iii)+'.jpg'

            image_path=os.path.join(self.path,filename)
            link=image['src']
            if link not in self.list:
                self.list.append(link)
                self.iii = self.iii + 1
            else:
                continue

            #response=requests.get(link,stream=True)
            try:
                response = requests.get(link, stream=True)
                with open(image_path,'wb') as file:
                    shutil.copyfileobj(response.raw,file)
            except Exception as e:
                print(e)
                #print('Could not downoald image number ',index)
                print('image link -->',link)
            print(image['src'])
    def log_in(self):
        user_name_input=self.driver.find_element_by_name("username")
        user_name_input.send_keys(self.username)
        password_input=self.driver.find_element_by_name("password")
        password_input.send_keys(self.password)
        password_input.submit()
    def open_target_profile(self):
        """search_bar=self.driver.find_element_by_css_selector('.XTCLo.x3qfX')
        search_bar.send_keys(self.target_username)
        sleep(3)
        f=self.driver.find_element_by_xpath('//span[@class="Fy4o8"]')
        f.click()"""
        sleep(3)
        X="michaeljackson"
        target_profile_url=self.main_url+'/'+self.target_username
        self.driver.get(target_profile_url)
        sleep(3)
    def scrroll_down(self):
        num_pub=self.driver.find_element_by_xpath('//span[@class="g47SY "]')
        num_pub=str(num_pub.text).replace(' ','')
        self.num_pub=int(num_pub)
        if self.num_pub>12:
            no_of_scrolls=int(self.num_pub/9)
            self.iii = 0
            for value in range(no_of_scrolls):
                print(value)
                sleep(1)
                self.downloading_images(self.iii)
                sleep(1)
                self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')

                sleep(1)
        print(num_pub)
if __name__=="__main__":
    app=App(target_username="lady.nettie")
    #app2= App(target_username="rachel_mypark")