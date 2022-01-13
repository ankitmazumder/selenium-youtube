from selenium import webdriver
from selenium.webdriver.chrome.options import Options
YOUTUBE_TRENDING_URL ='https://www.youtube.com/feed/trending'

def getDriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver
if __name__ == "__main__":
  driver=getDriver()

print('Fetching The page')

driver.get(YOUTUBE_TRENDING_URL)
print('Page Title: ',driver.title)
print('Get the video divs')
VIDEO_DIV_TAG = 'ytd-video-renderer'

video_divs = driver.find_elements_by_tag_name('VIDEO_DIV_TAG')

print(f'Found {len(video_divs)}videos')