from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from random import choice



option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})


usr = str()
pwd = str()

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
driver.get('https://www.facebook.com/')
sleep(8)

def login():
    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(3)
    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)
    print ("Password entered")
    sleep(3)
    password_box.send_keys(Keys.RETURN)
    print ("Logged In")
    sleep(5)


def friendreq(i):
    driver.get('https://www.facebook.com/')
    if i == 8:
        driver.close()
        driver.quit()
        print("tried adding friend multiple times, some error occured" )
    sleep(5)
    driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]/div[2]/div').click()
    sleep(6)
    driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div[1]/span').click()
    sleep(8)
    acc_loc_text = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/h2/span").text()
    search_bar = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/label/input")
    search_bar.send_keys(acc_loc_text)
    sleep(5)
    search_bar.send_keys(Keys.ENTER)
    people_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/a/div[1]/div[2]/div/div/div/div/span")
    sleep(3)
    people_button.click()
    add_frnd = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[3]/span/div").click()
    try:  # try to click Add Friend-button
        driver.find_element_by_partial_link_text('Add Friend').click()  # clicks Add Friend
        driver.get("https://www.facebook.com")  # reloads : facebook will not think that the script is a bot + time delay (new friends appear)
    except NoSuchElementException:  # if button not found
        sleep(8)  # wait (in hope that new Add Friend-buttons will appear)
        driver.get('https://www.facebook.com')
        i += 1
        if i >= 7:
            friendreq(i)


def story(con = "This is an automated story"):
    driver.get('https://www.facebook.com/stories/create')
    sleep(8)
    driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[2]').click()
    sleep(9)
    type_story = driver.find_element_by_xpath('//*[@id="jsc_c_k"]')
    type_story.send_keys(con)
    sleep(5)
    driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/div/span/span').click()


def comment(con = "This is an automated comment"):
    driver.get('https://www.facebook.com')
    driver.get('https://www.facebook.com') #refresh the page twice to get rid of sponsored posts on the top
    sleep(8)
    try:
        a = choice(range(1000, 6000, 1000))
        script = "window.scrollTo(0, "+str(a)+")"
        driver.execute_script(script)   #scroll to a random post
        sleep(4)
        commentBox = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div[1]/div/div/div/form/div/div/div[2]/div')
        commentBox.click()
        sleep(2)
        commentBox.send_keys(con)
        sleep(4)
        commentBox.send_keys(Keys.RETURN)
        sleep(20)
    except:
        a = 4000
        script = "window.scrollTo(0, " + str(a) + ")"
        driver.execute_script(script)  # scroll to a random post
        sleep(4)
        commentBox = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div[1]/div/div/div/form/div/div/div[2]/div')
        commentBox.click()
        sleep(2)
        commentBox.send_keys(con)
        sleep(4)
        commentBox.send_keys(Keys.RETURN)
        sleep(20)




