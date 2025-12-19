"""JobHawk Pro: Google Sheets Integration Module"""
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from logger import setup_logger

logger = setup_logger()
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('sheets', 'v4', credentials=creds)

def get_or_create_sheet(service, sheet_name: str):
    try:
        results = service.spreadsheets().get(pageSize=1, fields="spreadsheets(name)").execute()
        for s in results.get('spreadsheets', []):
            if s['name'] == sheet_name:
                return s['spreadsheetId']
    except Exception as e:
        logger.error(f"List error: {e}")
    body = {'properties': {'title': sheet_name}}
    new_sheet = service.spreadsheets().create(body=body).execute()
    logger.info(f"Created sheet: {sheet_name}")
    return new_sheet['spreadsheetId']

def append_to_sheet(service, spreadsheet_id: str, values, range_name: str = 'Sheet1!A1'):
    try:
        body = {'values': values}
        service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()
        logger.info("Data appended.")
    except Exception as e:
        logger.error(f"Append error: {e}")
