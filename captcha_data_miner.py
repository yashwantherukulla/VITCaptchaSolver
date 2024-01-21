from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
import data_url
import time
from PIL import Image
from io import BytesIO

#proxy_server_url = "103.6.223.2:3128"

options = webdriver.ChromeOptions()
#options.add_argument(f'--proxy-server={proxy_server_url}')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

for i in range(25,31):
    driver.get("https://vtop.vit.ac.in/vtop/")

    login_pg_open_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stdForm"]/a/div/div[2]/button')))
    login_pg_open_btn.click()

    captcha_location = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="captchaBlock"]/img')))
    raw_captcha_img_src = captcha_location.get_attribute("src")
    captcha_img_src = data_url.DataURL.from_url(raw_captcha_img_src)
    img = Image.open(BytesIO(captcha_img_src.data))
    img.save(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/c{i}.jpeg")
    time.sleep(2)