import sqlite3

def check_price_drop(url, current_price):
    conn = sqlite3.connect("prices.db")
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(price) FROM prices WHERE url = ?", (url,))
    min_price = cursor.fetchone()[0]
    conn.close()

    return float(current_price) < min_price if min_price else False
import csv
from database import init_db, get_products, save_price_to_db, add_product
from scraper import scrape_from_html
from email_alert import send_email

# Configure your email here
SENDER_EMAIL = "dheerajnani2255@gmail.com"
SENDER_PASSWORD = "vrqu wcgc wluq uiag"
RECEIVER_EMAIL = "dheerajnani2255@gmail.com"

def export_to_csv(title, price):
    with open("prices.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, price])

def run_tracker():
    init_db()
    products = get_products()

    for p in products:
        id, name, html, title_sel, price_sel, threshold = p

        result = scrape_from_html(html, title_sel, price_sel)
        if "error" in result:
            print(f"❌ Error for {name}: {result['error']}")
            continue

        title, price = result["title"], result["price"]
        print(f"✅ {title} → ₹{price}")

        # Save to DB and CSV
        save_price_to_db(id, title, price)
        export_to_csv(title, price)

        # Check threshold and alert
        if price < threshold:
            print("📬 Sending price drop email...")
            send_email(
                f"Price Drop Alert: {title}",
                f"The current price ₹{price} is below your threshold ₹{threshold}.",
                RECEIVER_EMAIL
            )


if __name__ == "__main__":
    # Example setup (run once to insert dummy products)
    init_db()
    add_product(
        name="NoiseFit Halo",
        html="<html><body><h1 class='product-title'>NoiseFit Halo</h1><span class='product-price'>₹4499</span></body></html>",
        title_selector="h1.product-title",
        price_selector="span.product-price",
        threshold_price=5000
    )
    add_product(
        name="Boat Rockerz",
        html="<html><body><h1 class='product-title'>Boat Rockerz 255</h1><span class='product-price'>₹1299</span></body></html>",
        title_selector="h1.product-title",
        price_selector="span.product-price",
        threshold_price=1000
    )

    run_tracker()
