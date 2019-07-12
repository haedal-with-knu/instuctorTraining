import requests

#lotto_round = requests.get('lotto_round')
#url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}"
#lottoround 수정 필요 일단 최신회차인 866회로 제작
url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
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