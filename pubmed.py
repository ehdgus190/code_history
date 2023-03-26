# https://pubmed.ncbi.nlm.nih.gov/?term={}&page={}


import requests
from bs4 import BeautifulSoup
import datetime

keyword = input("키워드 입력 : ")
allPage = input("몇 페이지까지 추출하겠습니까? : ")

for page in range(1, int(allPage) + 1):
    soup = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term={}&page={}'.format(keyword, page), headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(soup.text, 'html.parser')
    jobs = html.select('div.docsum-content')


    for job in jobs:
        try:
            today = datetime.datetime.now().strftime('%Y-%m-%d')

            company = job.select('a.docsum-title')[0].text.strip()
            print(company)

            # author = job.select('div.docsum-citation full-citation')

            pnids = job.select('span.citation-part > span')[0].text

            detailPage = 'https://pubmed.ncbi.nlm.nih.gov/' + pnids.strip()

            print(detailPage)

            soup_1 = requests.get(detailPage, headers={'User-Agent': 'Mozilla/5.0'})
            html_1 = BeautifulSoup(soup_1.text, 'html.parser')
            urls = html_1.select('div.abstract')
            for url in urls:
                try:
                    abstract = url.find('div', class_ = 'abstract-content selected')


                    abstract = abstract.find('p')
                    abstract = abstract.get_text().strip()
                    print(abstract)
                    # print(abstract)

                except Exception:
                    pass

        except Exception:
            pass

# import pandas as pd
#
# raw_data = pd.DataFrame.from_records([company])
# raw_data.to_excel(excel_writer='sample.xlsx')

# import csv
# with open('C:/Users/user/PycharmProjects/autocode/csv-savefile.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#
#     writer.writerow(['title', 'abstract'])
#
#     writer.writerows([
#         [company], [abstract]
#     ])
#
# # alt + shift + E : jupyter note 처럼 사용 가능.
