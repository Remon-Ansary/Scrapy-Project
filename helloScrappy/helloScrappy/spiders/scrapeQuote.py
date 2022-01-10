
import scrapy
import json
import psycopg2
conn = psycopg2.connect(dbname="first",user="postgres",password="root", host="localhost")
cur = conn.cursor()
# cur.execute("INSERT INTO table1 (title, price) VALUES (%s, %s)", ("hello", "ok"))

# cur.execute("CREATE TABLE newdata (id serial PRIMARY KEY, title varchar, price varchar, rating varchar, location varchar, amenities varchar,image varchar);")

class QuotesSpider(scrapy.Spider):

    name = "quotes"
    start_urls = [
        'https://www.kayak.co.in/Los-Angeles-Hotels.16078.hotel.ksp'
    ]

    def parse(self, response):
        for quote in response.css('.soom'):

            image = quote.xpath('a/img/@src').get()
            title = str(quote.xpath('div[1]/div/div/a/span/text()').get(), )
            if image is None:
                new = response.xpath(f"(//script[contains(text(),'{title}')])/text()").getall()
                files = json.loads(new[0])
                image = files.get('image')

                if image:
                    image = str(image)
                    price = str(quote.xpath('div/div/span/text()').get(), )
                    rating = str(quote.xpath('div/div/div/div/span/text()').get(), )
                    location = str(quote.css(
                        'div.soom-content-wrapper div.soom-description-wrapper div.soom-description div.soom-price-section span.soom-neighborhood::text').get(), )
                    amenities = str(quote.css(
                        'div.soom div.soom-content-wrapper div.soom-freebies-section div.soom-freebies div.soom-freebie span.yRv1-text::text').extract(), )
                    cur.execute(
                        "INSERT INTO newdata (title, price ,rating ,location ,amenities,image) VALUES (%s,%s,%s,%s,%s,%s)",
                        (title, price, rating, location, amenities, image))
                    conn.commit()
            else:
                image = str(image)
                price = str(quote.xpath('div/div/span/text()').get(), )
                rating = str(quote.xpath('div/div/div/div/span/text()').get(), )
                location = str(quote.css(
                    'div.soom-content-wrapper div.soom-description-wrapper div.soom-description div.soom-price-section span.soom-neighborhood::text').get(), )
                amenities = str(quote.css(
                    'div.soom div.soom-content-wrapper div.soom-freebies-section div.soom-freebies div.soom-freebie span.yRv1-text::text').extract(), )
                cur.execute(
                    "INSERT INTO newdata (title, price ,rating ,location ,amenities,image) VALUES (%s,%s,%s,%s,%s,%s)",
                    (title, price, rating, location, amenities, image))
                conn.commit()








