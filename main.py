import time, os, sys, requests, re
from bs4 import BeautifulSoup 
print('''
###################################
WELCOME TO ALPHA 0.0.2 of e621 1991
###################################
''')
a = 1
while True:
    code = input("INSERT A CODE:")
    headers = {"User-Agent":"LizzieTheWitch"}
    site0 = "https://e621.net/posts/"
    site = site0+code
    response = requests.get(site, headers=headers)
    api_key = "da3DG9QGd6qsyUp4htgqcs4B"
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]

    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        if not filename:
            print("Regex didn't match with the url: {}".format(url))
            continue
        with open(filename.group(1), 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)
