from selenium import webdriver

def setup_driver():
    """Sets up the Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment for headless mode
    driver = webdriver.Chrome(options=options)
    return driver