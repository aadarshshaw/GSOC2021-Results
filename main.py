from bs4 import BeautifulSoup
import csv

f = csv.writer(open("gsoc2021.csv",'w'))
f.writerow(['Name','Organization','Project'])

soup = BeautifulSoup(open("page.html"), features="lxml")

res = soup.findAll(class_='project-card__right-header-content')
names =[]
organizations = []
projects = []
for i in res:
    names.append(i.find('h2'))
    a = i.findAll('a')
    projects.append(a[0])
    organizations.append(a[1])
for i in range(len(names)):
    f.writerow([names[i].text,organizations[i].text,projects[i].text])


