import time  # Import time module
import pyttsx3  # Import pyttsx3 for text-to-speech
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Infow:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        
        self.engine = pyttsx3.init()

    def get_info(self, query):
        self.query = query
        self.driver.get('https://www.wikipedia.org')

        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()

        time.sleep(3)  

        # try:
        #     first_para = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]')
        #     paragraph_text = first_para.text
        #     print("First Paragraph: ", paragraph_text)

        #     self.speak(paragraph_text)

        # except Exception as e:
        #     print('Error in finding the paragraph:', e)

        # time.sleep(60)  

    def speak(self, text):
        self.engine.say(text)  
        self.engine.runAndWait() 

# if __name__ == "__main__":
#     assist = Infow()
#     assist.get_info("neutron stars")
