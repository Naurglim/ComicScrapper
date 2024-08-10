from bs4 import BeautifulSoup
import requests, os, html


def download_page(url, save_as):
    os.makedirs(os.path.dirname(save_as), exist_ok=True)
    #wget.download(url, save_as)
    response = requests.get(url)
    with open(save_as, 'wb') as file:
        file.write(response.content)


comic_site_url = "https://comixextra.com/"
comic_site_search = "search?keyword=critical+role"


comic_series_url = "critical-role-2017/"
comic_book_url = "issue-6/"

comic_book_full_url = os.path.join(comic_site_url, comic_series_url, comic_book_url,'full')
comic_book_full_path = os.path.join(comic_series_url, comic_book_url)

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







    





""" repository_url = "https://readcomicsonline.ru/uploads/manga"
comic_series = "critical-role-2017/chapters"
comic_book = "1"
comic_page = "01.jpg"

full_url = os.path.join(repository_url, comic_series, comic_book, comic_page)
print(full_url)

img_data = requests.get(full_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data) """