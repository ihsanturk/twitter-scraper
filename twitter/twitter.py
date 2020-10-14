import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Twitter:

	latest = True
	flag_latest = "&f=live"
	url_search = "https://twitter.com/search?q="

	# xpath_tweet = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]'
	# xpath_tweet = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[1]'
	xpath_tweet = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/div/section/div/div/div[2]'

	user_agent = "user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.65 Mobile/15E148 Safari/604.1',"

	def __init__(s, latest):
		s.latest = latest
		s.driver = webdriver.Firefox()
		s.wait = WebDriverWait(s.driver, 5)

	def search(s, query):
		url = s.url_search + query
		url += s.flag_latest if s.latest else ''
		sys.stderr.write(f"Sending requst to: {url}\n")
		s.driver.get(url)

		# FIXME:vim:vip
		tweets = s.wait.until(EC.presence_of_element_located((By.XPATH, s.xpath_tweet)))
		# tweets = s.driver.find_elements(By.XPATH, s.xpath_tweet)

		return s.driver.page_source

		# NOTE: selenium examples
		# s.driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
		# print(first_result.get_attribute("textContent"))
		# return s.driver.get_current_page()

