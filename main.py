"""🌟 JOBHAWK PRO v1.0 - Launch Control & Orchestrator"""
import json
import sys
import time
from scraper import scrape_indeed
from sheets import authenticate, get_or_create_sheet, append_to_sheet
from logger import setup_logger

logger = setup_logger()

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("config.json missing.")
        sys.exit(1)

def main():
    logger.info("🌟 JOBHAWK PRO: Mission launch.")
    config = load_config()
    jobs = scrape_indeed(config['search_term'], config['location'], config['max_jobs'])
    if not jobs:
        logger.warning("No jobs found.")
        return
    service = authenticate()
    spreadsheet_id = get_or_create_sheet(service, config['sheet_name'])
    header = ['Title', 'Company', 'Location', 'Link', 'Date Added']
    values = [header] + [[j['Title'], j['Company'], j['Location'], j['Link'], j['Date Added']] for j in jobs]
    append_to_sheet(service, spreadsheet_id, values, config['sheet_range'])
    logger.info(f"✅ {len(jobs)} jobs saved.")
    print(f"\n📊 Sheet: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

if __name__ == '__main__':
    main()
