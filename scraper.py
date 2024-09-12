import requests
from bs4 import BeautifulSoup
import csv

def scrape_products(url, output_csv):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example selectors; adjust according to the website's structure
    products = soup.find_all('div', class_='product')
    
    data = []
    for product in products:
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('span', class_='product-price').text.strip()
        rating = product.find('span', class_='product-rating').text.strip()
        
        data.append([name, price, rating])
    
    # Save to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Rating'])
        writer.writerows(data)
    
    print(f"Data successfully saved to {output_csv}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python scraper.py <url> <output_csv>")
        sys.exit(1)
    
    url = sys.argv[1]
    output_csv = sys.argv[2]
    scrape_products(url, output_csv)
