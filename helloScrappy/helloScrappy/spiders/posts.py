import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"
    test = 'San-Francisco-Hotels.13852.hotel.ksp'
    start_urls = [
        'https://www.kayak.co.in/Hyderabad-Hotels.7297.hotel.ksp' + test

    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)