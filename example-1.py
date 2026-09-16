import requests
from bs4 import BeautifulSoup
import csv

evler = []
for i in range(1,6):

    url = f"https://www.accommodationforstudents.com/london/student-halls?page={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    houses = soup.find_all("article",class_='carousel ImageCarousel__wrapper--2da3a CardBase__card--7bbff PropertyGridPage__item--f51cb')
    for item in houses:
        name = item.find("h3",class_='CardBase__title--11645').text.strip()
        location = item.find("p",class_="CardBase__textRow--5d0e7 CardBase__address--fe9fa CardBase__addressTitleCased--fb2f2").text.strip()
        price = item.find("div",class_="CardBase__rentAndRoomOptionsWrapper--5b1d4").find("strong",class_="CardBase__rentPrice--436ce").text.strip()
        try:
            rooms = item.find("div",class_="CardBase__roomOptionsText--e16ba").find("strong").text.strip()
        except:
            rooms = "NOT GIVEN"
        url ="https://www.accommodationforstudents.com"+ item.find("a").get("href")
        evler.append({"Name":name,"Location":location,"Price":price,"Rooms":rooms,"Link":url})


csv_file = "houses.csv"
fieldnames = ["Name", "Price","Location","Rooms", "Link"]
with open(csv_file, mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(evler)
