from scrapy import Request, Spider


class GameJamsSpider(Spider):
    name = "game_jams"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.pages = int(kwargs.get("pages", 10))

    def start_requests(self):
        for i in range(1, self.pages + 1):
            yield Request(f"https://itch.io/jams/past?page={i}")

    def parse(self, response):
        for jam in response.xpath(".//div[@class='jam lazy_images']"):
            yield {
                "title": jam.xpath(".//h3/a/text()").get(),
                "hosted_by": '|'.join(jam.xpath(".//div[@class='hosted_by meta_row']/a/text()").getall()),
                "ended": jam.xpath(".//span[@class='date_countdown']/@title").get(),
                "no_of_participants": jam.xpath(".//div[@class='jam_stats']/div/span/text()").get(),
                "no_of_submissions": jam.xpath(".//div[@class='jam_stats']/a/span/text()").get(),
                "ranked": self.get_ranked(jam),
                "featured": self.get_featured(jam),
            }

    def get_ranked(self, jam) -> bool:
        ranked_text = jam.xpath(".//div[@class='jam_ranked']/strong/text()").get()
        return True if ranked_text == " Ranked" else False


    def get_featured(self, jam) -> bool:
        featured_text = jam.xpath(".//div[@class='featured_flag']/text()").get()
        return True if featured_text == "Featured" else False
