import requests
from bs4 import BeautifulSoup

r = requests.get('https://dhlottery.co.kr/common.do?method=main').text
print(r)
soup = BeautifulSoup(r,'html.parser')
lotto_round = soup.find('strong', id='lottoDrwNo').text


#lotto_round = requests.get('lotto_round')
url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}"
response = requests.get(url)
# response.text # => string
lotto = response.json() # => dict
print(lotto)
winner = []

# list comprehension
# a = [n*2 for n in range(1, 7)] # => [2, 4, 6, 8, 10, 12]
a = [lotto[f'drwtNo{n}'] for n in range(1, 7)]
bonus = lotto['bnusNo']
winner = f'{a} + {bonus}'
print(winner)

