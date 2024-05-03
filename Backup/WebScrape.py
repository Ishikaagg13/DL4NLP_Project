from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

url = "https://nationalmuseumindia.gov.in/en/collections/index/6"
class_1 = "swiper-slide swiper-slide-next"

all_urls = [f"https://nationalmuseumindia.gov.in/en/collections/index/{num}" for num in range(6,17)]
driver = webdriver.Chrome()


data = []

for links in all_urls:
    driver.get(links)
    art_links = driver.find_elements(By.XPATH, "//a[@class='modal-pop']")
    for links in art_links:
        try:
            title = links.get_attribute("title")
            img = links.find_element(By.XPATH, ".//img").get_attribute("src")
            print(title,img)

            data.append({'Title':title,'Image':img})
        except:
            print('No description available')

        


print(data.count)
pd.DataFrame(data).to_csv('data.csv')