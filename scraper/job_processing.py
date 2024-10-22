from bs4 import BeautifulSoup
import csv

def extract_jobs(driver):
    """Extracts job information from the loaded LinkedIn page."""
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_cards = soup.find_all('a', class_='base-card__full-link')

    jobs = []
    for job_card in job_cards:
        job_link = job_card.get('href', 'No link available')  # Use 'get()' for safe extraction with default value
        job_info = job_card.find_parent('li')

        # Use 'get_text()' with default fallback and chaining to avoid explicit if-else checks
        title = job_info.find('h3', class_='base-search-card__title').get_text(strip=True) if job_info else "No title available"
        company = job_info.find('h4', class_='base-search-card__subtitle').get_text(strip=True) if job_info else "No company name available"
        location = job_info.find('span', class_='job-search-card__location').get_text(strip=True) if job_info else "Location not available"

        jobs.append((title, company, location, job_link))

    return jobs

def save_jobs_to_csv(jobs, filename='linkedin_jobs.csv'):
    """Saves the scraped jobs to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title', 'Company', 'Location', 'Job Link'])
        writer.writerows(jobs)