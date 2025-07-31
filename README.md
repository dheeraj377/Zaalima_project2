# Price Monitoring and Web Scraping Application

## Project Overview

This Python project is designed to monitor prices of products listed on e-commerce platforms by scraping product information from static HTML pages. 
The tool allows users to define a threshold price for each product, and if the current price drops below the threshold, an email alert is sent. 
All product data is stored in an SQLite database and also exported to a CSV file. 
This is particularly useful for users who want to track price drops over time without manually checking websites.

## Features

- Scrape product names and prices from HTML pages
- Track multiple products simultaneously
- Compare current price with a user-defined threshold
- Store product data in a local SQLite database
- Export tracked product data to a CSV file
- Display product information in a tabular format in the terminal
- Send email alerts when prices fall below the threshold

## Technologies Used

- Python 3.10 or above
- BeautifulSoup for HTML parsing
- SQLite for local database storage
- Pandas for CSV export and table formatting
- smtplib and email.mime for sending emails


## Sample Output

Product Name         Price     Threshold
---------------------------------------
NoiseFit Halo        4499.0    5000.0
Price drop detected. Sending email...
Email sent successfully.
Data saved to database and product_prices.csv


## Author
# Dheeraj Kumar Jeripothula
Electrical and Electronics Engineering Student
Zaalima Intern
