# Webscraping Stealth Scraper

A Python-based web scraper designed to extract job listings with stealth features to avoid detection. The scraper collects job information and exports the data to both CSV and JSON formats.

## Features

- **Stealth Mode**: Implements anti-detection techniques including:
  - Rotating user agents
  - Random delays between requests
  - Proper HTTP headers
  - Retry mechanism with exponential backoff
  
- **Multiple Export Formats**: Saves scraped data in both CSV and JSON formats for easy data analysis and integration

- **Error Handling**: Robust error handling to skip problematic entries and retry failed requests

- **Clean Data Extraction**: Extracts key job information including title, company, location, and posting date

## Prerequisites

Before running the scraper, ensure you have Python 3.6+ installed along with the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/TMR1905/Webscraping-Stealthscraper.git
cd Webscraping-Stealthscraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the scraper using:

```bash
python scraper_final.py
```

The script will:
1. Connect to the target website with stealth features
2. Extract job listings
3. Save the data to `jobs.csv` and `jobs.json`

## Output

The scraper generates two files:

- **jobs.csv**: Comma-separated values file with columns: title, company, location, date
- **jobs.json**: JSON formatted data with the same information

### Example Output

```json
[
  {
    "title": "Software Engineer",
    "company": "Example Corp",
    "location": "Remote",
    "date": "2025-12-01"
  }
]
```

## Configuration

You can modify the scraper by adjusting:

- `max_retries`: Number of retry attempts for failed requests (default: 3)
- User agents list: Add more user agent strings for better rotation
- Delay range: Adjust the `time.sleep(random.uniform(1,2))` values for different timing

## Ethical Use

This scraper is for educational purposes. When using web scraping tools:

- Always respect robots.txt
- Don't overload servers with requests
- Follow the website's terms of service
- Use scraped data responsibly

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## Troubleshooting

**Issue**: Connection timeout or 403 errors  
**Solution**: The website may be blocking requests. Try increasing the delay between requests or updating the user agent list.

**Issue**: Missing data in output  
**Solution**: The website structure may have changed. Check the CSS selectors in the `scrape_jobs()` function.