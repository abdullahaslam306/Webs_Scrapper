import scrapy
import csv


class BookSpider(scrapy.Spider):
    name = 'books'
    csvfile = open('book-data.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter='\t')
    i = 1
    writer.writerow(["SN","Author","Title","Description","Keywords"])

    def start_requests(self):
        folder = "http://localhost:80/csbooks/"
            #path of website
        urls = [
            'Books-1.html',
            'Books-2.html',
            'Books-3.html',
        ]

        for url in urls:
            yield scrapy.Request(url=folder+url, callback=self.parse)
            #request website address

    def addqoute(self,value):
        value="'"+value+"'"
        return value

    def parse(self, response):

        books = response.xpath("//div[@class='book']")
        print(books.getall())
        for book in books:
            title = book.xpath(".//div[@class='title']/text() ").extract_first()
            author = book.xpath(".//div[@class='author']/text()").extract_first()
            description = book.xpath(".//div[@class='description']/text()").extract_first()
            keywords = ", ".join(book.xpath(".//div[@class='keywords']/span[@class='tag']/text()").extract())
            author=author.replace("by ", "")
            author = author.replace("(Author)", "").strip()

            self.writer.writerow([self.i, self.addqoute(author),self.addqoute(title), self.addqoute(description), self.addqoute(keywords)])
            self.i+= 1

