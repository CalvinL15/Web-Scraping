# README

Requirements to run the code: 
- python3 with the following modules installed: bs4, requests, and urllib.

How to run:
- Use this command: python3 "GetDownloadableFiles.py" "argv2"
- "argv2" can either be an url or a text file containing list of urls, where a line contains one url.

Then, the script will generate a new directory named "result" which will be used to store the downloaded files.
- If "argv2" is an url, there will be only two further directories created inside "result": "result_pdf" and "result_img".
- "result_pdf" will contain pdf file(s) downloaded from the targeted url and "result_img" will contain the image(s) downloaded.
- If "argv2" is a txt file, there will be 2 + 2*n more directories created, where n = number of valid urls inside the txt file. 
- The first two directories created are "result_pdf" and "result_img" which will be located inside the "result" folder.
- Then, for other directories, they will be created inside "result_pdf" and "result_img" with naming convention below: 
  - "result_1", "result_2", ...., "result_n".
- Each of "result_pdf" and "result_img" will have n files.
