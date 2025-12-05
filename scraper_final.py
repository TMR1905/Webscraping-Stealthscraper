import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import random

def stealth_request(url, max_retries=3):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Firefox/89.0"
    ]

    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }

    for attempt in range(max_retries):
        try:
            time.sleep(random.uniform(1,2))
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
    return None

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = stealth_request(url)
    
    if not response:
        print("Failed to fetch page")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.select("div.card-content")
    
    jobs = []
    for card in job_cards:
        try:
            job = {
                "title": card.select_one("h2.title").text.strip(),
                "company": card.select_one("h3.company").text.strip(),
                "location": card.select_one("p.location").text.strip(),
                "date": card.select_one("time").text.strip()
            }
            jobs.append(job)
        except AttributeError as e:
            print(f"Skipping job card - missing data: {e}")
            continue            
    
    return jobs

# Test it
def save_to_csv(jobs, filename="jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "company", "location", "date"])
        writer.writeheader()
        writer.writerows(jobs)
    print(f"Saved {len(jobs)} jobs to {filename}")

def save_to_json(jobs, filename="jobs.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2)
    print(f"Saved {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    print("Starting job scraper...")
    
    jobs = scrape_jobs()
    
    if jobs:
        save_to_csv(jobs)
        save_to_json(jobs)
        print(f"\nDone! Scraped {len(jobs)} jobs.")
    else:
        print("No jobs found.")