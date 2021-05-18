import requests
import csv

f = csv.writer(open("gsoc2021.csv","w"))
f.writerow(["Name","Organization","Project"])
page_no=1

while True:
    s= f"https://summerofcode.withgoogle.com/api/program/current/project/?page={page_no}&page_size=20"
    res = requests.get(s)
    j=res.json()
    page_no+=1
    if len(j["results"]) ==0:
        break
    for idx in range(len(j["results"])):
        current = j['results'][idx]
        project = current['title']
        name = current['student']['display_name']
        organization = current['organization']['name']
        f.writerow([name,organization,project])
    
