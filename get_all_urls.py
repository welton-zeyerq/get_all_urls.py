#!/usr/bin/env python3
import sys
import logging
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")
try:
    from bs4 import BeautifulSoup
except:
    sys.exit("Install missing library: pip install bs4")

if len(sys.argv) !=5:
    if len(sys.argv) !=3:
        if len(sys.argv) !=2:
            print("follow the example:")
            print("")
            print("%s -u https://www.site.com.br -s /home/user/Documents/get_all_urls.txt"%(sys.argv[0]))
            sys.exit()

try:
    choice = str(sys.argv[3])
    if choice == "-s":
        LOG = sys.argv[4]
        logging.basicConfig(level=logging.INFO, filename=LOG, format="%(message)s")

    elif choice == "--save":
        LOG = sys.argv[4]
        logging.basicConfig(level=logging.INFO, filename=LOG, format="%(message)s")

    else:
        print("ERROR, NO OPTION OR DIGITATION ERROR")

except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)

try:
    choice = str(sys.argv[1])
    if choice == "-u":
        url = sys.argv[2]
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, "html.parser")

        urls = []
        for link in soup.find_all("a"):
            print(link.get("href"))
            logging.info(link.get("href"))

    elif choice == "-h":
        print("follow the examples:")
        print("")
        print("%s -u https://www.site.com.br -s /home/user/Documents/get_all_urls.txt"%(sys.argv[0]))

    elif choice == "--help":
        print("follow the examples:")
        print("")
        print("%s -u https://www.site.com.br -s /home/user/Documents/get_all_urls.txt"%(sys.argv[0]))

    else:
        print("ERROR, NO OPTION OR DIGITATION ERROR")

except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)




