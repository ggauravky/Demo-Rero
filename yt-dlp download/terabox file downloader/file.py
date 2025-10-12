from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests

# Replace this with the link you want to download
link = "https://terasharelink.com/s/1qRAjeBgzc_roZAkqwg7YzQ"

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Set up ChromeDriver (Make sure chromedriver is in your PATH or use webdriver-manager)
driver = webdriver.Chrome(service=Service(), options=options)

try:
    driver.get(link)

    # Wait for download button (adjust timeout and check actual text if needed)
    wait = WebDriverWait(driver, 20)
    download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download')]")))

    file_url = download_button.get_attribute('href')
    print("Found file URL:", file_url)

    # Optional: Download using requests
    if file_url:
        response = requests.get(file_url, stream=True)
        filename = file_url.split("/")[-1] or "downloaded_file"

        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"✅ Download complete: {filename}")
    else:
        print("❌ Could not extract download link.")

except Exception as e:
    print("⚠️ Error occurred:", str(e))

finally:
    time.sleep(3)
    driver.quit()
