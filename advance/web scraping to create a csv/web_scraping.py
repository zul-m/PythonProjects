# Import the necessary packages.
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;as-pos=0&amp;as-type=HISTORY&amp;as-searchtext=sa"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

# To see how many HTML containers are present in the link.
containers = page_soup.findAll("div", { "class": "_3O0U0u"})

print(len(containers))

print(soup.prettify(containers[0]))

# To see the first item present in the page.
container = containers[0]

print(container.div.img["alt"])

# To look at the price of this smartphone.
price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})

print(price[0].text)

# To look at its ratings from its customers.
ratings = container.findAll("div", {"class": "niH0FQ"})

print(ratings[0].text)

# Create a CSV file and store all the mobile phones with their name, price and ratings.
filename = "products.csv"
f = open(filename, "w")
headers = "Product_Name, Pricing, Ratings \n"
f.write(headers)

# To look at what our CSV file has stored after the web scraping of Flipkart.
for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating = rating_container[0].text
    print("Product_Name:"+ product_name)
    print("Price: " + price)
    print("Ratings:" + rating)