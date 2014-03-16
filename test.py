import requests
import bs4
import urlparse

url = "http://www.binghamtonudining.com/dailymenus.php"
parsed = urlparse.urlparse(url)
base_url = "{}://{}".format(parsed.scheme, parsed.netloc)

soup = bs4.BeautifulSoup(requests.get(url).text)

intermediate_links = []
for elem in soup.find_all("a"):
    link = elem.attrs["href"]
    link = link.replace("\n", "").replace("\t", "")
    intermediate_links.append(link)

links = []
for intermed in intermediate_links:
    links.append(urlparse.urljoin(base_url, intermed))

calendars = []
for link in links:
    calendars.append(bs4.BeautifulSoup(requests.get(link).text))
