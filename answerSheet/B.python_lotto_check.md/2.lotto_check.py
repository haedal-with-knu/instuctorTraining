import requests

lotto_round = request.args.get('lotto_round')
url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}"
response = requests.get(url)
# response.text # => string
lotto = response.json() # => dict
winner = []

# list comprehension
# a = [n*2 for n in range(1, 7)] # => [2, 4, 6, 8, 10, 12]
a = [lotto[f'drwtNo{n}'] for n in range(1, 7)]
bonus = lotto['bnusNo']
winner = f'{a} + {bonus}'