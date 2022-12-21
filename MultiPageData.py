from bs4 import BeautifulSoup as ds
import requests
import pandas as pd
def ins(url_link):
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",}
    r = requests.get(url_link)
    req = r.content
    return ds(req, "lxml")
txt = lambda tag:tag.get_text(' ',strip=True) if tag else ""
url = "https://subslikescript.com/movies_letter-A?page=1"
base ="https://subslikescript.com/"
df =pd.DataFrame(columns=["name","Link","Plot"])
soup = ins(url)
c=1
while soup.find("nav",class_="pagination_pages").find("a",class_="page-link",href=True):
    url = f"https://subslikescript.com/movies_letter-A?page={c}"
    soup = ins(url)
    li = soup.find("ul",{"class":"scripts-list"}).find_all("a")
    for i in li:
        r=[]
        n = txt(i)
        a= str(base+i["href"])
        r.append(n)
        r.append(a)
        s1 = ins(a)
        r.append(txt(s1.find("p",{"class":"plot"})))
        df.loc[len(df)]=r
        
        
    c+=1
df.to_csv("Movies.csv")


