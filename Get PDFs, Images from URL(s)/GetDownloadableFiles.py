from bs4 import BeautifulSoup
# from urllib.parse import urlparse, urljoin
from urllib.parse import urlparse, urljoin
import requests
import sys
import os

def is_valid(url):	#check whether url is valid or not
	parsed = urlparse(url)
	return bool(parsed.netloc) and bool(parsed.scheme)

def getPDF(url):
	req = requests.get(url)
	#print(req)
	html_page = req.content
	soup = BeautifulSoup(html_page, 'html.parser')
	pdf_links = []
	for link in soup.select("a[href$='.pdf']"):
		pdf_url = urljoin(url, link['href'])
		#print(pdf_url)
		pdf_links.append(pdf_url)	
	return pdf_links		

def getImages(url):
	req = requests.get(url)
	#print(req)
	html_page = req.content
	soup = BeautifulSoup(html_page, 'html.parser')
	image_urls = []
	for img in soup.find_all("img"):
		img_url = img.attrs.get("src")
		if not img_url:
			continue
		img_url = urljoin(url, img_url)
		try: #getting the position of '?' character and remove everything after it
			position = img_url.index("?")
			img_url = img_url[:pos]
		except ValueError:
			pass
		if is_valid(img_url):
			image_urls.append(img_url)		
	return image_urls

def download(url, path):
	response = requests.get(url, stream=True)
	file_size = int(response.headers.get("Content-Length", 0))
	filename = os.path.join(path, url.split("/")[-1])
	print(filename)
	f = open(filename, "wb")
	for data in response.iter_content(1024):
		f.write(data)
	f.close()	
		
if __name__ == "__main__":
	print("This is a script to get the downloadable files (img or pdf) from an url ...")
	if(len(sys.argv) < 2):
		print("Need more argument(s)!")
	elif (len(sys.argv) == 2 and is_valid(sys.argv[1])):
		if not os.path.exists("result_pdf"):
			os.mkdir("result_pdf")
		if not os.path.exists("result_img"):
			os.mkdir("result_img")
		pdfs = getPDF(sys.argv[1])
		for pdf in pdfs:
			download(pdf, "result_pdf")
		images = getImages(sys.argv[1])
		for img in images:
			download(img, "result_img")		
	else:
		if not os.path.exists("result_pdf"):
			os.mkdir("result_pdf")
		if not os.path.exists("result_img"):
			os.mkdir("result_img")
		file = open(sys.argv[1], "r")
		url_list = file.read().splitlines()
		count = 0	
		for url in url_list:
			count += 1
			if(is_valid(url)):
				subdir_pdf = "result_pdf//result_" + str(count)
				subdir_img = "result_img//result_" + str(count)
				if not os.path.exists(subdir_pdf):
					os.mkdir(subdir_pdf)
				if not os.path.exists(subdir_img):	
					os.mkdir(subdir_img)
				pdfs = getPDF(url)
				for pdf in pdfs:
					download(pdf, subdir_pdf)
				images = getImages(url)	
				for img in images:
					download(img, subdir_img)
			else:
				count -= 1	

		file.close()
	print("Task completed!")					

