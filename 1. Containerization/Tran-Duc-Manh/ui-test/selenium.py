import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)
def create_driver_with_proxy():
    # Tạo tùy chọn của trình duyệt Chrome với proxy ngẫu nhiên đã chọn
    chrome_options = Options()
    driver = webdriver.Chrome(
        chromedriver_autoinstaller.install(), options=chrome_options
    )
    return driver


def run_selenium_task():
    TEST_INPUT = {
        "name":"test",
        "university":"BKHN",
        "title":"KHMT",
        "year":2022
    }
    driver = create_driver_with_proxy()
    driver.get(f"https://api.viettelcloud.site/")
    time.sleep(1)
    try:
        add_button = driver.find_element(By.ID, "addUserButton")
        add_button.click()
        time.sleep(1)
        add_button = driver.find_element(By.ID, "nameID")
        add_button.send_keys(TEST_INPUT['name'])
        add_button = driver.find_element(By.ID, "titleID")
        add_button.send_keys(TEST_INPUT['title'])
        add_button = driver.find_element(By.ID, "yearID")
        add_button.send_keys(TEST_INPUT['year'])
        add_button = driver.find_element(By.ID, "universityID")
        add_button.send_keys(TEST_INPUT['university'])
        add_button = driver.find_element(By.ID, "submitButton")
        add_button.click()
        time.sleep(10)
        logger.info("Pass the add user test")

    except:
        logger.info("Fail the add user test")

def run_update_task():
    TEST_INPUT = {
        "name":"test",
        "university":"Update title",
        "title":"Update title",
        "year":1998
    }
    driver = create_driver_with_proxy()
    driver.get(f"https://api.viettelcloud.site/user/test")
    time.sleep(1)
    try:
        add_button = driver.find_element(By.ID, "addUserButton")
        add_button.click()
        time.sleep(1)
        add_button = driver.find_element(By.ID, "titleID")
        add_button.send_keys(TEST_INPUT['title'])
        add_button = driver.find_element(By.ID, "yearID")
        add_button.send_keys(TEST_INPUT['year'])
        add_button = driver.find_element(By.ID, "universityID")
        add_button.send_keys(TEST_INPUT['university'])
        add_button = driver.find_element(By.ID, "submitButton")
        add_button.click()
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "about")))
        finally:
            time.sleep(2)
            driver.quit()
        logger.info("Pass the add update test")

    except:
        logger.info("Fail the update user test")

def run_delete_task():
    TEST_INPUT = {
        "name":"test",
        "university":"BKHN",
        "title":"KHMT",
        "year":2022
    }
    driver = create_driver_with_proxy()
    driver.get(f"https://api.viettelcloud.site/user/test")
    time.sleep(2)
    try:
        add_button = driver.find_element(By.ID, "deleteButton")
        add_button.click()
        time.sleep(2)
        logger.info("Pass the delete user test")

    except:
        logger.info("Fail the delete user test")

if __name__ == "__main__":
    run_selenium_task()
    run_update_task()
    run_delete_task()