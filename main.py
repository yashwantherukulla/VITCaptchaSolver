from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
import data_url
import time
from PIL import Image
from io import BytesIO

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_extension('D:/tech/Coding/python/python_projects/VIT CourseEnroller/ViBoot src/ViBoot.crx')
driver = webdriver.Chrome(options=options)

driver.get("https://vtop.vit.ac.in/vtop/")

uname = 'YASHWANTH500'
pwd = 'Potato@198'



login_pg_open_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stdForm"]/a/div/div[2]/button')))
login_pg_open_btn.click()

uname_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
uname_field.send_keys(uname)

pwd_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
pwd_field.send_keys(pwd)

submit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="submitBtn"]')))
submit_btn.click()

captcha_location = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="captchaBlock"]/img')))
raw_captcha_img_src = captcha_location.get_attribute("src")
captcha_img_src = data_url.DataURL.from_url(raw_captcha_img_src)
img = Image.open(BytesIO(captcha_img_src.data))
img.show()
img.save('captcha.jpeg')

