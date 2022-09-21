#!/usr/bin/env python
import requests
def request(url):
    try:
        return requests.get("http://"+url)

    except requests.exceptions.ConnectionError:
        pass
target_url = "192.168.29.97/mutillidae"

with open("common.txt","r") as word_list:
    for list in word_list:
        word = list.strip()
        test_url = target_url +"/"+ word
        response = request(test_url)
        if response:
            print("[+] Discover URL --> "+ test_url)