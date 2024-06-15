import requests as rq
import logging

logger = logging.getLogger('RequestsLogger')



sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    # ДОПОЛНИТЬ КОД ЗДЕСЬ >>> я решил не дополнять а сделать отдельный под себя >>> файл start.py
    response = rq.get(site, timeout=3)
    print(response)
