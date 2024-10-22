from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def dismiss_sign_in_modal(driver):
    """Dismisses the LinkedIn sign-in modal if it appears."""
    sleep(10)
    try:
        dismiss_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal__dismiss"))
        )
        dismiss_button.click()
        print("Dismissed the sign-in modal.")
    except (NoSuchElementException, TimeoutException):
        print("No sign-in modal found.")

def scroll_up_and_down(driver, times, scroll_pause_time=1):
    """Performs scroll up and down motions to load more content."""
    for _ in range(times):
        driver.execute_script("window.scrollBy(0, -500);")
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        sleep(scroll_pause_time)

def scroll_and_find_button(driver, scroll_pause_time):
    """Scrolls and looks for the 'See more jobs' button, keeps trying until found."""
    while True:
        try:
            see_more_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".infinite-scroller__show-more-button--visible"))
            )
            print("Button found! Stopping scroll and attempting to click.")
            return see_more_button
        except TimeoutException:
            print("Button not found, performing scroll up and down.")
            driver.execute_script("window.scrollBy(0, -500);")  # Scroll up 500 pixels
            sleep(1)
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            sleep(scroll_pause_time)

def click_button(see_more_button):
    """Attempts to click the 'See more jobs' button multiple times."""
    for attempt in range(5):
        try:
            see_more_button.click()
            print(f"Clicked 'See more jobs' button. Attempt {attempt + 1}/5.")
            return True
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            print(f"'See more jobs' button not clickable on attempt {attempt + 1}.")
            break
    return False