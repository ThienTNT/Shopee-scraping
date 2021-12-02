# Basic Shopee-scraping

This is my practice scraping just for fun.<br>
Have inspiration from "Scrape Amazon.com".<br>
I'm Vietnamese so my English might not be good enough. So if there are any mistakes, please forgive me.<br>

**Description: When you run this program, it will open 1 web browser of your and navigate to shopee page.
After that, it will scrape all necessary information from the page based on your search keyword.
Then wait for a moment and the program will save all scraped information to the file ShopeeText.txt in the same directory.**

# Guide how to use

1. Install Python 3
2. Install bs4 and selenium library
3. Download the corresponding driver of your web browser
4. Put that driver into your project folder
5. Run the program and have fun

### A little about my process:
I'm using Google Chrome ver 96.0.4664.45.<br>
This is the page where I downloaded the driver: https://chromedriver.chromium.org/downloads <br>

My computer is a bit weak, so I adjusted the time sleep a bit longer to load the page. You can adjust it to run faster, so you don't have to waste time waiting.<br>
Edit time sleep at line: 64, 67.<br>
Edit range at line 62 to scrape more pages. 