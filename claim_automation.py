import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import WebDriverException

# ---------------------------
# Configurations
# ---------------------------

CHROME_USER_DATA_DIR = r"C:\Users\Ahmad Alqudah\AppData\Local\Google\Chrome\User Data"
CHROME_PROFILES = ["Profile 9", "Profile 10"]

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
BRAVE_USER_DATA_DIR = r"C:\Users\Ahmad Alqudah\AppData\Local\BraveSoftware\Brave-Browser\User Data"

EDGE_USER_DATA_DIR = r"C:\Users\Ahmad Alqudah\AppData\Local\Microsoft\Edge\User Data"
EDGE_PROFILE = "Default"

TARGET_URL = "https://dashboard.3dos.io/home/dashboard"


# ---------------------------
# Function to claim reward
# ---------------------------

def claim_reward(driver, browser_name):
    try:
        driver.get(TARGET_URL)
        print(f"🌐 Opened URL in {browser_name}")
        time.sleep(5)

        # Find and click CLAIM button
        claim_button = driver.find_element(By.XPATH, "//button[contains(text(), 'CLAIM REWARD')]")
        claim_button.click()
        print(f"✅ {browser_name}: Claimed reward!")
    except Exception as e:
        print(f"⚠️ {browser_name}: Failed to claim reward – {e}")
    finally:
        time.sleep(2)
        driver.quit()


# ---------------------------
# Launch Chrome profiles
# ---------------------------

for profile in CHROME_PROFILES:
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-data-dir={CHROME_USER_DATA_DIR}")
        chrome_options.add_argument(f"profile-directory={profile}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        claim_reward(driver, f"Chrome ({profile})")

    except WebDriverException as e:
        print(f"🚫 Chrome ({profile}): Could not launch – {e}")


# ---------------------------
# Launch Brave
# ---------------------------

try:
    brave_options = webdriver.ChromeOptions()
    brave_options.binary_location = BRAVE_PATH
    brave_options.add_argument(f"user-data-dir={BRAVE_USER_DATA_DIR}")
    brave_options.add_argument("--no-sandbox")
    brave_options.add_argument("--disable-dev-shm-usage")
    brave_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=brave_options)
    claim_reward(driver, "Brave")

except WebDriverException as e:
    print(f"🚫 Brave: Could not launch – {e}")


# ---------------------------
# Launch Edge
# ---------------------------

try:
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument(f"user-data-dir={EDGE_USER_DATA_DIR}")
    edge_options.add_argument(f"profile-directory={EDGE_PROFILE}")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--disable-gpu")

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    claim_reward(driver, "Edge")

except WebDriverException as e:
    print(f"🚫 Edge: Could not launch – {e}")
