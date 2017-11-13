from bs4 import BeautifulSoup




soup = BeautifulSoup(open("lobanovskiy.html"),"lxml")
mydivs = soup.findAll("a", { "class" : "elsewhere-website" })

for i in mydivs:
    print i["class"]
    print i['data-url']