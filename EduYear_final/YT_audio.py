import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Music():
    def __init__(self):
        # Set up ChromeDriver with the correct Service object
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def play(self, query):
        self.query = query
        # Construct the YouTube search URL
        self.driver.get(f"https://www.youtube.com/results?search_query={query}")

        try:
            # Wait for the first video to load and find the video title link and click it
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]/yt-formatted-string'))
            )

            # Find the first video and click
            video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
            video.click()

            # Wait for the video to load and play for a minute
            print("Playing the video...")
            time.sleep(60)  # Keep the tab open for 1 minute

        except Exception as e:
            print(f"Error in playing video: {e}")

# if __name__ == "__main__":
#     assist = Music()
#     assist.play('believer')
