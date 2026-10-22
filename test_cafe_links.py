
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path
import time

options = Options()
options.binary_location = (
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
)

driver = webdriver.Chrome(options=options)

try:
    # Open the HTML file from the same folder as this script
    html_file = Path(__file__).resolve().parent / "cafe_link_test.html"
    print("HTML file exists:", html_file.exists())
    print("HTML path:", html_file)

    driver.get(html_file.as_uri())
    time.sleep(1)

    print("Website title:", driver.title)
    print("Current URL:", driver.current_url)

    # Check whether the Menu link exists
    links = driver.find_elements(By.CSS_SELECTOR, "a[data-page='menu']")
    print("Menu links found:", len(links))

    if links:
        links[0].click()
        time.sleep(1)

        section = driver.find_element(By.ID, "menu")
        print("Menu section displayed:", section.is_displayed())

        if section.is_displayed():
            print("TEST CASE PASS")
        else:
            print("TEST CASE FAIL")
    else:
        print("TEST CASE FAIL: Menu link not found.")

    input("Press Enter to close browser...")

finally:
    driver.quit()
