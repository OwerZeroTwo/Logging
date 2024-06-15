import logging
import requests

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Create log files
success_log = logging.getLogger('success')
success_log.setLevel(logging.INFO)
success_handler = logging.FileHandler('success_responses.log')
success_handler.setLevel(logging.INFO)
success_log.addHandler(success_handler)

bad_log = logging.getLogger('bad')
bad_log.setLevel(logging.WARNING)
bad_handler = logging.FileHandler('bad_responses.log')
bad_handler.setLevel(logging.WARNING)
bad_log.addHandler(bad_handler)

blocked_log = logging.getLogger('blocked')
blocked_log.setLevel(logging.ERROR)
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_handler.setLevel(logging.ERROR)
blocked_log.addHandler(blocked_handler)

# List of URLs to check
urls = [
    'https://www.youtube.com/',
    'https://wikipedia.org',
    'https://yahoo.com',
    'https://yandex.ru',
    'https://whatsapp.com',
    'https://amazon.com',
    'https://www.ozon.ru',
    'https://instagram.com',
    'https://twitter.com'
]

# Check each URL
for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            success_log.info(f"'{url}', response - {response.status_code}")
        else:
            bad_log.warning(f"'{url}', response - {response.status_code}")
    except requests.exceptions.RequestException:
        blocked_log.error(f"{url}, NO CONNECTION")