# Usage

## Step 1: Setup ChromeDriver

1. Download the ChromeDriver that matches your Chrome browser version.
2. Place the `chromedriver` executable in your PATH or in the root directory of the project.
3. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Step 2: Modify Scraping Parameters

You can modify the maximum number of jobs to scrape by editing the max_jobs variable in the main() function inside main.py:

max_jobs = 500  # Adjust the number of jobs you want to scrape

You can change the link in main.py to get your desired job and filther

driver.get("https://www.linkedin.com/jobs/search/")

## Step 3: Customizing the Code

If you want to customize or extend the scraping functionality, the code is organized into modular functions located in the scraper/ directory. Feel free to modify the individual files for navigation, job extraction, or output customization.

## Step 4: Run the Scraper

To run the scraper, use the following command:

```bash
python main.py
```

Notes

	•	LinkedIn might block excessive scraping activity, so it’s advised to add reasonable pauses between requests.
	•	Ensure that you comply with LinkedIn’s Terms of Service when using this scraper.