from config import PRODUCT_URLS, TARGET_PRICE, IMAGE_FOLDER
from scraper import scrape_product
from image_downloader import download_image
from price_checker import check_price

print("=" * 50)
print("      PRODUCT WEB SCRAPER")
print("=" * 50)

for url in PRODUCT_URLS:

    product = scrape_product(url)

    if product:

        image_path = download_image(
            product["image"],
            product["title"],
            IMAGE_FOLDER
        )

        status = check_price(
            product["price"],
            TARGET_PRICE
        )

        print("\nProduct Title :", product["title"])
        print("Price :", product["price"])
        print("Image URL :", product["image"])
        print("Image Saved :", image_path)
        print("Status :", status)
        print("-" * 50)