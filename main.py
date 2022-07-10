from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
best_movies_page = response.text

soup = BeautifulSoup(best_movies_page, "html.parser")


titles_scraped = [title.text for title in soup.find_all(name="h3", class_="title")]
titles = "\n".join(titles_scraped[::-1]) # slicing operator for reversing lists or strings
                                         # n.join function separates each item in new line
with open("titles.txt", "w", encoding="utf8") as titles_text:
    titles_text.write(titles)

# print(titles)
