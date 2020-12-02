from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import sys
import os

def getElements(url, count):
	req = requests.get(url)
	html_page = req.content
	soup = BeautifulSoup(html_page, 'html.parser')
	if count != 0:
		filename = "result//page" + str(count) + ".txt"
	else:
		filename = "result//page" + ".txt"	
	f = open(filename, "w")
	f.write(str(soup.prettify()))
	f.close()
	return

def is_valid(url):	#check whether url is valid or not
	parsed = urlparse(url)
	return bool(parsed.netloc) and bool(parsed.scheme)

if __name__ == "__main__":
	print("HTML Text Extractor Tool with Python ...")
	if(len(sys.argv) < 2):
		print("Need more argument(s)!")
	elif (len(sys.argv) == 2 and is_valid(sys.argv[1])):
		if not os.path.exists("result"):
			os.mkdir("result")
		getElements(sys.argv[1], 0)
		print("Task completed!")
	else:
		if not os.path.exists("result"):
			os.mkdir("result")
		f = open(sys.argv[1], "r")
		count = 0
		while True:
			count += 1	
			line = f.readline()
			if line:
				if(is_valid(line)):
					getElements(line, count)
				else:
					filename = "page" + str(count) + ".txt"
					file = open(filename, "w")
					file.write("Invalid format!")
					file.close()
			if not line:
				break
		f.close()
		print("Task completed!")
