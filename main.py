import time
from scraper import setup_driver, dismiss_sign_in_modal, scroll_and_find_button, click_button, scroll_up_and_down, extract_jobs, save_jobs_to_csv

def main():
    start_time = time.time()  # Start the timer

    driver = setup_driver()
    driver.get("https://www.linkedin.com/jobs/search/?keywords=Data%20Scientist&location=United%20States&f_TPR=r604800&f_E=1%2C2%2C3%2C4&currentJobId=4056124667&position=1&pageNum=0")

    dismiss_sign_in_modal(driver)

    jobs = []
    max_jobs = 500
    scroll_pause_time = 2

    while len(jobs) < max_jobs:
        see_more_button = scroll_and_find_button(driver, scroll_pause_time)

        if see_more_button:
            button_clicked = click_button(see_more_button)
            if button_clicked:
                scroll_up_and_down(driver, 3)

        new_jobs = extract_jobs(driver)
        jobs.extend(new_jobs)

        jobs = list({job[3]: job for job in jobs}.values())  # Remove duplicates by job link

        print(f"Total jobs scraped so far: {len(jobs)}")

        if len(jobs) >= max_jobs:
            break

    driver.quit()

    save_jobs_to_csv(jobs)

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    print(f"Total jobs scraped: {len(jobs)}")
    print(f"Time taken to complete: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()