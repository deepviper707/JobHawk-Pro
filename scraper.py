"""JobHawk Pro: Indeed Job Scraper Engine"""
import requests
from bs4 import BeautifulSoup
import time
from utils import hash_job, get_user_agent
from logger import setup_logger

logger = setup_logger()

def scrape_indeed(search_term: str, location: str, max_jobs: int = 15, retries: int = 3):
    url = "https://www.indeed.com/jobs"
    params = {'q': search_term, 'l': location, 'fromage': 7, 'start': 0, 'limit': max_jobs}
    jobs = []
    seen_hashes = set()

    for attempt in range(retries):
        headers = {"User-Agent": get_user_agent()}
        try:
            logger.info(f"Fetching jobs: '{search_term}' in '{location}'")
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            break
        except requests.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2)
    else:
        logger.error("All retries failed.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.find_all('div', class_='job_seen_beacon')

    for card in job_cards[:max_jobs]:
        try:
            title = card.select_one('h2.jobTitle span').text.strip() if card.select_one('h2.jobTitle span') else "N/A"
            company = card.select_one('span[data-testid="company-name"]').text.strip() if card.select_one('span[data-testid="company-name"]') else "N/A"
            location_val = card.select_one('div[data-testid="job-location"]').text.strip() if card.select_one('div[data-testid="job-location"]') else "N/A"
            link_elem = card.select_one('a[data-testid="job-link"]')
            link = 'https://www.indeed.com' + link_elem['href'] if link_elem else "N/A"

            job_hash = hash_job(title, company, link)
            if job_hash in seen_hashes: continue
            seen_hashes.add(job_hash)

            jobs.append({
                'Title': title,
                'Company': company,
                'Location': location_val,
                'Link': link,
                'Date Added': time.strftime('%Y-%m-%d %H:%M:%S')
            })
        except Exception as e:
            logger.warning(f"Parse error: {e}")

    logger.info(f"Scraped {len(jobs)} unique jobs.")
    return jobs
