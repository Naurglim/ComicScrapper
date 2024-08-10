import os
import requests 
from bs4 import BeautifulSoup


COMIC_SITE_BASE_URL = "https://comixextra.com/"
COMIC_SITE_SEARCH = "search?keyword="
COMIC_SITE_SEARCH_URL = COMIC_SITE_BASE_URL + COMIC_SITE_SEARCH
COMIC_SITE_SEARCH_SEPARATOR = "+"
FOLDER = "comics"


def download_page(url, save_as):
    os.makedirs(os.path.dirname(save_as), exist_ok=True)
    response = requests.get(url)
    with open(save_as, 'wb') as file:
        file.write(response.content)


def get_keywords_result(search):
    res = []
    
    keywords = search.split()
    search_string = COMIC_SITE_SEARCH_SEPARATOR.join(keywords)
    url = COMIC_SITE_SEARCH_URL + search_string

    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")
    result_list = soup.find_all("div", class_="cartoon-box")
    for results in result_list:
        title_details = results.select_one("div.mb-right > h3 > a")
        value = {
            "title": title_details.text.strip(),
            "url": title_details['href'].strip()
        }
        res.append(value)
    return res


def get_title_issues(url):
    res = []
    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")
    episode_list = soup.find("div", class_="episode-list")
    issues = episode_list.select("div > table.table > tbody > tr > td > a")
    for issue in issues:
        value = {
            "title": issue.text.strip(),
            "url": issue['href'].strip()
        }
        res.append(value)
    return res


def download_issue(comic_book_url, comic_book_full_path):
    comic_html = requests.get(comic_book_url + '/full')
    soup = BeautifulSoup(comic_html.content, "html.parser")
    chapter_container = soup.find_all("div", class_="chapter-container")
    for chapter in chapter_container:
        pages = chapter.find_all("img")
        i = 1
        for page in pages:
            page_name = str(i).zfill(2)+'.jpg'
            page_filename = os.path.join(comic_book_full_path, page_name)
            page_url = page["src"].strip()
            download_page(page_url, page_filename)
            i += 1
    print('compressing: ' + comic_book_full_path)


title_list = get_keywords_result('critical role')

for title in title_list:
    title_folder = os.path.basename(os.path.normpath(title['url']))
    issue_list = get_title_issues(title['url'])
    for issue in issue_list:
        issue_folder = os.path.basename(os.path.normpath(issue['url']))
        file_path = os.path.join(FOLDER, title_folder, issue_folder)
        print("Downloading: " + issue['url'])
        download_issue(issue['url'], file_path)


""" 

comic_series_url = "critical-role-2017/"
comic_book_url = "issue-6/"

comic_book_full_url = os.path.join(COMIC_SITE_BASE_URL, comic_series_url, comic_book_url,'full')
comic_book_full_path = os.path.join(FOLDER, comic_series_url, comic_book_url)

comic_html = requests.get(comic_book_full_url)
soup = BeautifulSoup(comic_html.content, "html.parser")

chapter_container = soup.find_all("div", class_="chapter-container")
for chapter in chapter_container:
    pages = chapter.find_all("img")
    i = 1
    for page in pages:
        page_name = str(i).zfill(2)+'.jpg'
        page_filename = os.path.join(comic_book_full_path, page_name)
        page_url = page["src"].strip()
        download_page(page_url, page_filename)
        i += 1
 """

""" repository_url = "https://readcomicsonline.ru/uploads/manga"
comic_series = "critical-role-2017/chapters"
comic_book = "1"
comic_page = "01.jpg"

full_url = os.path.join(repository_url, comic_series, comic_book, comic_page)
print(full_url)

img_data = requests.get(full_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data) """