import requests
from bs4 import BeautifulSoup

def scrape_product(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch:", url)
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text

    price = soup.find("p", class_="price_color").text
    price = float(price.replace("£", "").replace("Â", ""))

    image = soup.find("img")["src"]
    image = "https://books.toscrape.com/" + image.replace("../", "")

    return {
        "title": title,
        "price": price,
        "image": image
    }