import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(class_="a-size-large product-title-word-break").get_text().strip()

product_link = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

content = f"Title: {title}\nCurrent Price: ${price_as_float}\nProduct link: {product_link}"

if price_as_float < 100:
    import smtplib

    my_email = "ghostyyyyyghost@gmail.com"
    password = "vgfuivloajnbbunh"

    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()

        connections.login(user=my_email, password=password)
        connections.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: PRICE DROP!\n\n{content}".encode("utf-8")
        )