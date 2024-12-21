import requests
from bs4 import BeautifulSoup
import csv

# 웹페이지 가져오기
webpage = requests.get("https://pyony.com/search/")
soup = BeautifulSoup(webpage.content, "html.parser")

# 마지막 페이지 추출
page = soup.findAll("a", {"class": "page-link"})
last_page = page[-1].get('href')
_last_page = int(last_page.replace("?page=", ""))

print("Last page:", _last_page)

# 결과 저장할 리스트
all_results = []

# 페이지별 크롤링
for x in range(1, _last_page + 1):
    if len(all_results) >= 80:
        break

    webpage = requests.get(f"https://pyony.com/search/?page={x}")
    soup = BeautifulSoup(webpage.content, "html.parser")

    for j in range(20):
        try:
            category = soup.findAll("small", {"class": "float-right font-weight-bold"})[j].get_text()
            if category == "생활용품":
                continue

            obj = soup.findAll("div", {"class": "card-body"})[j].get_text().replace(" ", "").replace("\n", "|").split("|")
            _obj = []
            i = 0
            for val in obj:
                if val:
                    if i < 4:
                        _obj.append(val)
                        i += 1

            img = soup.findAll("img", {"class": "prod_img"})[j].get('src')
            _obj.append(img)

            all_results.append(_obj)

            if len(all_results) >= 80:
                break

        except IndexError:
            break

csv_filename = "pyony_filtered_data.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Price", "Description", "Extra", "Image URL"])
    writer.writerows(all_results)
