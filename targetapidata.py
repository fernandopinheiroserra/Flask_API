from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

base_url = "https://www.shipstation.com/docs/api/"

# Configure Selenium to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

visited_urls = set()
endpoints = []

def crawl_page(url):
    if url in visited_urls:
        return

    driver.get(url)
    html_content = driver.page_source

    soup = BeautifulSoup(html_content, "html.parser")

    # Extract endpoint information from the current page if available
    endpoints_section = soup.find("div", {"id": "endpoints"})
    if endpoints_section:
        for endpoint_row in endpoints_section.find_all("tr"):
            cells = endpoint_row.find_all("td")
            if len(cells) >= 4:
                method = cells[0].text.strip()
                path = cells[1].text.strip()
                description = cells[2].text.strip()
                endpoint = {
                    "method": method,
                    "path": path,
                    "description": description
                }
                endpoints.append(endpoint)

    # Add the current URL to the visited set
    visited_urls.add(url)

    # Find links in the sidebar navigation menu
    sidebar_links = driver.find_elements_by_css_selector(".menu li a")

    for link in sidebar_links:
        child_url = link.get_attribute("href")

        # Recursively crawl the child page
        crawl_page(child_url)

# Start crawling from the initial page
crawl_page(base_url)

# Print the gathered endpoints
for endpoint in endpoints:
    print(f"Method: {endpoint['method']}")
    print(f"Path: {endpoint['path']}")
    print(f"Description: {endpoint['description']}")
    print()