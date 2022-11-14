#!/usr/bin/env python3
import sys
import time
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")
try:
    from bs4 import BeautifulSoup
except:
    sys.exit("Install missing library: pip install bs4")
import logging

def help_gau():
    print("follow the examples: ")
    print()
    print("%s -h"%(sys.argv[0]))
    print("%s --help"%(sys.argv[0]))
    print("%s -u https://www.site.com.br --save /home/user/Documents/get_all_urls.txt"%(sys.argv[0]))
    sys.exit()

if len(sys.argv) <=1:
    help_gau()
    sys.exit()
elif len(sys.argv) ==2:
    choice = str(sys.argv[1])
    if choice == "-u":
        print("insert valid url")
        sys.exit()
    elif choice == "-h":
        help_gau()
        sys.exit()
    elif choice == "--help":
        help_gau()
        sys.exit()
    else:
        print("invalid option")
        print()
        help_gau()
        sys.exit()
elif len(sys.argv) ==3:
    print("insert save-file output")
    sys.exit()
elif len(sys.argv) ==4:
    choice = str(sys.argv[3])
    if choice == "--save":
        print("insert save-file output")
        sys.exit()
    else:
        print("invalid option")
        print()
        help_gau()
        sys.exit()
elif len(sys.argv) >=6:
    print("incorrect parameters")
    sys.exit()
else:
    pass

LOG = sys.argv[4]
logging.basicConfig(level=logging.INFO, filename=LOG, format="%(message)s")

try:
    if __name__ == "__main__":
        url = sys.argv[2]
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, "html.parser")
except Exception as error:
    pass
except requests.exceptions.Timeout:
    time.sleep(5)
    pass
except requests.exceptions.TooManyRedirects:
    print("url error")
    pass
except requests.exceptions.RequestException as error:
    print(error)
except KeyboardInterrupt:
    sys.exit()

urls = []
for link in soup.find_all("a"):
    print(link.get("href"))
    logging.info(link.get("href"))

