import requests
from bs4 import BeautifulSoup
from configs import HEADERS
import redis

base_video_url = 'https://bbs.hupu_crawler.com/4858-{}'


# res = requests.get(url, timeout=3, headers=HEADERS)

def parse_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    soup.find_all('ul', {''})


class Hupu_Video_crawler:
    def __init__(self):
        self.client = redis.Redis()
        self.url_list = []

    def run(self):
        pass

    def get_video_html(self, page_nums=50):
        for page_index in range(1, page_nums):
            html = requests.get(base_video_url.format(page_index))
            assert requests.status_codes == 200


bs = BeautifulSoup(res.text, 'html.parser')
video_url = bs.find('video')['src']

res = requests.get(video_url, headers=HEADERS, stream=True)

with open('play.video', 'wb') as f:
    for chunk in res.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()
