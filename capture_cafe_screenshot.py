
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

# Configure Brave browser
options = Options()
options.binary_location = (
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    # Open the Cafe Management System test page
    project_folder = Path(__file__).resolve().parent
    html_file = project_folder / "cafe_link_test.html"

    driver.get(html_file.as_uri())

    # Capture and save the screenshot
    screenshot_path = project_folder / "cafe_screenshot.png"
    success = driver.save_screenshot(str(screenshot_path))

    if success:
        print("Screenshot is captured successfully.")
        print("Saved at:", screenshot_path)
    else:
        print("Screenshot capture failed.")

finally:
    driver.quit()
