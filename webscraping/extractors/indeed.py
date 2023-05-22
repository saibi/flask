# bot blocked

#from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

base_url= "https://kr.indeed.com/jobs?q="
search_term = "python"

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
browser = webdriver.Chrome(options=options)
browser.get(f"{base_url}{search_term}&limit=50")

print(browser.page_source)

