# LinkedIn Scraper

This is a Python-based web scraper designed to extract job listings from LinkedIn. It automates the process of scrolling through job listings, clicking the "See more jobs" button, and extracting relevant information such as job title, company name, location, and job link. The scraped data is saved in a CSV file for further analysis.

## Features

- Automatically scrolls through LinkedIn job listings.
- Clicks the "See more jobs" button to load more listings.
- Extracts job title, company name, location, and job link.
- Saves the scraped data to a CSV file.
- Handles LinkedIn's sign-in modal if it appears.

## Prerequisites

Before running the scraper, make sure you have the following installed:

- Python 3.8 or later
- [Google Chrome](https://www.google.com/chrome/) (latest version)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (compatible with your Chrome version)
- [Selenium](https://www.selenium.dev/) library
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing

You can install the necessary Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Note

Go into incognito mode without signing in on linkedin, type in the job, and the filther you want. Then copy the link and paste it main.py, driver.get().