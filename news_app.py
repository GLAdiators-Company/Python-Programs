import requests
import json
query = input('What type of news are you interested in ?')
r = requests.get(f'https://newsapi.org/v2/everything?q={query}&from=2023-09-10&sortBy=publishedAt&apiKey=3bbe93f5d87046e9a67bc9e9721e94df')

result = json.loads(r.text)
for article in result['articles']:
    print('Title : '+article['title'])
    print('Description : '+article['description'])
    print('----------------------------------------------------------------')