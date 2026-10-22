
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.binary_location = (
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
)

driver = webdriver.Chrome(options=options)

try:
    driver.get(
        "file:///C:/Users/akary/OneDrive/Desktop/CafeManagement/cafe_link_test.html"
    )

    time.sleep(2)

    # 1. Maximize the browser
    driver.maximize_window()
    print("Browser maximized successfully.")
    time.sleep(3)

    # 2. Try fullscreen mode
    try:
        driver.fullscreen_window()
        print("Browser entered fullscreen mode.")
    except Exception as e:
        print("Fullscreen mode is not supported:", e.msg.splitlines()[0])

    time.sleep(3)

    # 3. Set a custom browser size
    driver.set_window_rect(width=1500, height=400)
    print("Custom window size applied.")
    time.sleep(3)

    # 4. Retrieve actual window dimensions
    dimensions = driver.get_window_size()

    print("Actual height:", dimensions["height"])
    print("Actual width:", dimensions["width"])

finally:
    driver.quit()
