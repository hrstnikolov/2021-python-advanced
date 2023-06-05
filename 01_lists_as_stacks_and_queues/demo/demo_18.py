ll = [5, 2, 8, 7]
ll2 = [5, 2, 8, 7]
ll3 = [5, 2, 8, 7]
ll4 = [5, 2, 8, 7]
ll5 = [5, 2, 8, 7]

# променяне на списък докато итерираме върху него
# списъкът се променя динамично
for el in ll:
    ll.pop()
    print(el)
print()

# използвайки итератор, същият се изчислява само веднъж,
# остава непроменен въпреки промяната на списъка
for el in range(len(ll2)):
    ll2.pop()
    print(el)
print()

# фунцкията от списъка се изчислява на всяка итерация
i = 0
while i < len(ll3):
    ll3.pop()
    print(i)
    i += 1
print()

# функцията мап се преизчислява на всяка итерация
for el in map(str, ll4):
    ll4.pop()
    print(el)
print()

# list comprehension копира списъка, т.е. създава нов обект
for el in ll5[:]:
    ll5.pop()
    print(el)

'''
5
2

0
1
2
3

0
1

5
2

5
2
8
7
'''