import pandas as pd

data = pd.read_csv("C:/Users/siseo1/python/cook.csv", encoding='utf-8')

from selenium import webdriver

import time

driver = webdriver.Chrome("C:/Users/siseo1/python/chromedriver.exe")

url = "https://whereispost.com/keyword/"

driver.get(url)

element = driver.find_element_by_name('keyword')

for i in range(1,500):

	if i < 40:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 40:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 80:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 80:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 120:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 120:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 160:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 160:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 200:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 200:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 240:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 240:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 280:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 280:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 320:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 320:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 360:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 360:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 400:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 400:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i < 440:

		element.send_keys(data['Keyword'].iloc[i])

		element.submit()

		time.sleep(5)

	elif i == 480:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 480:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 520:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 520:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 560:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 560:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 600:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 600:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 640:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 640:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 680:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 680:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 720:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 720:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 760:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 760:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 800:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 800:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 840:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 840:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 880:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 880:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 920:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 920:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 960:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 960:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1000:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1000:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1040:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1040:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1080:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1080:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1120:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1120:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1160:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1160:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1200:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1200:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1240:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1240:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1280:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1280:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1320:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1320:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1360:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1360:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1400:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1400:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1440:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1440:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
	elif i == 1480:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)

	elif i == 1480:

		posting = driver.find_element_by_xpath('//*[@id="excel"]')

		posting.click()

		driver.get(url)

		element = driver.find_element_by_name('keyword')

		time.sleep(5)
