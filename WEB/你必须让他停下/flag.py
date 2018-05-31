#!/usr/bin/python3

from bs4 import BeautifulSoup

import requests

for i in range(100):
	res = requests.get("http://120.24.86.145:8002/web12/")
	res.encoding = "utf-8"
	soup = BeautifulSoup(res.text,"html.parser")
	print("src:"+str(i)+"  "+soup.select("a")[0].text)