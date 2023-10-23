
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class infow():
    def __init__(self):
        service = Service(executable_path="C:\\Users\\LENOVO\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe") 
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service , options=options)
    
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element("xpath",'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        enter.click()
        

        


