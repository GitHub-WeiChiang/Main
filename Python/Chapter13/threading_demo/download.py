__author__ = "ChiangWei"
__date__ = "2022/5/31"

from urllib.request import urlopen


def download(inner_url: str, file: str):
    with urlopen(inner_url) as u, open(file, 'wb') as f:
        f.write(u.read())


urls = [
    'https://openhome.cc/Gossip/Encoding/',
    'https://openhome.cc/Gossip/Scala/',
    'https://openhome.cc/Gossip/JavaScript/',
    'https://openhome.cc/Gossip/Python/'
]

filenames = [
    'Encoding.html',
    'Scala.html',
    'JavaScript.html',
    'Python.html'
]

for url, filename in zip(urls, filenames):
    download(url, filename)
