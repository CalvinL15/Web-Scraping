# README

Requirements to run the code: 
- python3 with the modules bs4, requests, colorama, and urllib installed.

How to run:
- Use this command: python3 "TextExtractor.py" "argv2"
- "argv2" can either be an url or a text file containing list of urls, where one line contains one url


Then, the script will generate a new directory named "result" and the result(s) will be written into new txt files located in the result directory.
The naming format:
- If there is only one url to be processed, it would be named "page.txt"
- If there are multiple urls, the output would be named: "page1.txt", "page2.txt", ... "page{n}.txt", where n = number of urls to be processed.

    
