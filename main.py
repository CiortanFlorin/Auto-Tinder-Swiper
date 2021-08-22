from selenium import webdriver
import time

chrome_driver_path = "E:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://tinder.com/")
time.sleep(1)

#Login
driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
time.sleep(2)
driver.find_element_by_css_selector('button._9o-t').click()
driver.find_element_by_id("email").send_keys("YOUR EMAIL")
driver.find_element_by_id("pass").send_keys("YOUR PASSWORD")
driver.find_element_by_name("login").click()
driver.switch_to.window(base_window)
time.sleep(5)

#Disable Pop-ups
driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[2]/div/div/div[1]/button').click()
time.sleep(5)

for n in range(0,10):
    if n==0:
        driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button').click()
        time.sleep(2)
        continue
    driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button').click()
    time.sleep(2)

