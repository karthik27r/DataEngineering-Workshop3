import psycopg2
import requests
import re
from bs4 import BeautifulSoup

# db_name = 'member_db'
# db_user = 'postgres'
# db_pass = '123456'
# db_host = 'psql-db'
# db_port = '5432'

# conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)

# def scrape_data(version, date, url):
#     sql = """INSERT INTO members_release (version, date, url) VALUES (%s, %s::DATE,%s))"""
    
#     with conn:
#             with conn.cursor() as cur:
#                 cur.execute(sql,(version, date, url))

# def truncate_table():
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute("TRUNCATE members_release CASCADE;")
def extract():
    print("Extraction starting")
    url ="https://pypi.org/project/requests/#history"
    
    #truncate_table()
    urldata=requests.get(url)
    recvHtml = urldata.content
    bsObj = BeautifulSoup(recvHtml, 'html.parser')
    
    for data in bsObj.find_all("div", class_="release"):
        
        url = data.find('a')
        urlText = url.get('href')
        #urlText = url.get('href')
        print("\n url: https:/"+urlText+"")
        
        version = data.find("p",class_="release__version")
        verText = version.text
        print("version: \n",verText)
        
        date = data.find("p",class_="release__version-date")
        dateText = date.text
        print("date: \n",dateText)
        
       
        
        
        
if __name__ == "__main__":
    extract()