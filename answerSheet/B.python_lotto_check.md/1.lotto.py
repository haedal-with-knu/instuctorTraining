import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
print(lotto)
print(f'오늘의 행운의 로또는 {sorted(lotto)} 입나다') #sorted()함수는 리스트를 정렬한 새로운 리스트를 반환

print(lotto) #sorted()함수는 리스트 자체를 변화시키진 않는다는 것을 확인

print(f'오늘의 행운의 로또는 {lotto.sort()} 입니다') #sort() 메소드는 반환값이 없다
print(lotto) #sort() 메소드는 리스트 자체를 정렬한다.