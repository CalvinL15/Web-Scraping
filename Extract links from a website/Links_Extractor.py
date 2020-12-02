from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import colorama
import requests

colorama.init()
GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
RESET = colorama.Fore.RESET

internal_urls = set()
external_urls = set()

def is_valid(url):
	parsed = urlparse(url)
	return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
	urls = set()
	domain_name = urlparse(url).netloc
	soup = BeautifulSoup(requests.get(url).content, "html.parser")
	for a_tag in soup.findAll('a'):
		href = a_tag.attrs.get('href')
		if href == "" or href is None:
			continue
		href = urljoin(url, href)
		#remove HTTP GET parameters
		parsed_href = urlparse(href)	
		href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
		if not is_valid(href):
			continue
		if href in internal_urls:
			continue
		if domain_name not in href:
			if href not in external_urls:
				print(f"{RED}[!] External link: {href}{RESET}")
				external_urls.add(href)
			continue
		print(f"{GREEN}[*] Internal link: {href}{RESET}")
		urls.add(href)
		internal_urls.add(href)

total_urls_visited = 0

def crawler(url, max_urls = 100):
	global total_urls_visited
	total_urls_visited += 1
	links = get_all_website_links(url)
	if links is not None:
		for link in links:
			if total_urls_visited > max_urls:
				break
			crawler(link, max_urls = max_urls)

if __name__ == "__main__":
	print("Links Extractor Tool with Python ...")
	print("Input your url:", end=" ")
	url = input()
	crawler(url, max_urls = max_urls)
	print("[+] Total Internal links: ", len(internal_urls))
	print("[+] Total External links: ", len(external_urls))	
	print("[+] Total links: ", len(internal_urls) + len(external_urls))
	 # save the internal links to a file
    with open(f"{domain_name}_internal_links.txt", "w") as f:
        for internal_link in internal_urls:
            print(internal_link.strip(), file=f)
    # save the external links to a file
    with open(f"{domain_name}_external_links.txt", "w") as f:
        for external_link in external_urls:
            print(external_link.strip(), file=f)



	
