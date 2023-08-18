from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
referer = "https://moviesmod.vip/"
chrome_options.add_argument(f"referer={referer}")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://moviesmod.vip/page/582/")
images =driver.find_elements(By.CSS_SELECTOR,'img.attachment-sociallyviral-featuredbig')
for image in images:
    img_src = image.get_attribute('src')

count = driver.find_elements(By.CSS_SELECTOR,'article.latestPost.excerpt')
tp_ocp= len(count)
a_elements = driver.find_elements(By.CSS_SELECTOR, "h2.title.front-view-title a")
checker = 1

# Loop through the <a> elements and get their 'href' attributes
for a_element in a_elements:
    if checker == tp_ocp:
        break

    href_value = a_element.get_attribute("href")
    print("href attribute:", href_value)
    driver.get(href_value)
    ul_element = driver.find_element(By.CSS_SELECTOR, "ul")
    li_elements = ul_element.find_elements(By.CSS_SELECTOR, "li")
    for li in li_elements:
        text = li.text
        if 'Name' in text and 'Size' in text:
            start_index = text.index('Name') + len('Name')
            end_index = text.index('Size')
            movie_descrp = text[start_index:end_index].strip()
            print(movie_descrp)
    a_elements = driver.find_elements(By.CSS_SELECTOR, "h2.title.front-view-title a")
    for a_element in a_elements:
        href_value = a_element.get_attribute("href")
        print(href_value)

    tp_ocp=1
