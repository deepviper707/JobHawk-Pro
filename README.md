```markdown
# 🌟 JobHawk Pro

Automated Indeed job scraper that saves results to Google Sheets.

Hunt smarter, not harder. 🦅

## Features

- Scrapes Indeed.com for jobs
- User-agent rotation & retry logic
- Duplicate prevention
- Appends results to Google Sheets with timestamps
- Clean, modular Python code

## Requirements

- Python 3.8+
- Google account

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/jobhawk-pro.git
cd jobhawk-pro
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Google API Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use existing)
3. Enable **Google Sheets API**
4. Go to Credentials → Create Credentials → OAuth client ID
5. Application type: **Desktop app**
6. Download the JSON file → Rename to `credentials.json`
7. Place `credentials.json` in the project folder

> **Never commit `credentials.json` or `token.json` to Git!** They are ignored via `.gitignore`.

### 5. Configure Your Search
Edit `config.json`:
```json
{
  "search_term": "data analyst",
  "location": "remote",
  "max_jobs": 15,
  "sheet_name": "JobHawk Pro - Active Targets",
  "sheet_range": "Sheet1!A1"
}
```

### 6. Run the Tool
```bash
python main.py
```

- First run: Browser opens → Sign in with Google → Allow access
- `token.json` is created automatically (no need to re-authenticate later)

## Output

Jobs are appended to your Google Sheet. The script prints the sheet URL at the end.

Example columns:  
Title | Company | Location | Link | Date Added

## Automation (Optional)

Run daily with cron (Linux/macOS):
```bash
crontab -e
```
Add:
```
0 9 * * * cd /path/to/jobhawk-pro && /path/to/venv/bin/python main.py >> jobhawk.log 2>&1
```

## Troubleshooting

- No jobs found → Try broader terms or "remote"
- Google auth issues → Delete `token.json` and re-run
- Scraping fails → Indeed may temporarily block; wait and retry

## Security Note

- `credentials.json` and `token.json` are git-ignored
- For personal use only

## License

MIT License

---

Happy hunting! 💼
```
```
