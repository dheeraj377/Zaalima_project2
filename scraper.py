from bs4 import BeautifulSoup

def scrape_from_html(html, title_selector, price_selector):
    soup = BeautifulSoup(html, "html.parser")
    try:
        title = soup.select_one(title_selector).get_text(strip=True)
        price_text = soup.select_one(price_selector).get_text(strip=True)
        price = float(''.join(c for c in price_text if c.isdigit() or c == '.'))
        return {"title": title, "price": price}
    except Exception as e:
        return {"error": str(e)}
