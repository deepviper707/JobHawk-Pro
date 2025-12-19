"""JobHawk Pro: Tactical Utilities Toolkit"""
import hashlib
import random

def hash_job(title: str, company: str, link: str) -> str:
    key = f"{title}|{company}|{link}".encode('utf-8')
    return hashlib.md5(key).hexdigest()

def get_user_agent() -> str:
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    ]
    return random.choice(agents)
