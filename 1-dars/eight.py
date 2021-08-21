# 8-Dars
# Sana: 17.08.2021
# Ko`chiruvchi: ALEVcoder

# cars = ['damas', 'malibu', 'traktor', 'kamaz', 'spark']
# print(cars) #Tartiblanmagan holda
# cars.sort()
# print(cars) #Tartiblangan holda

# cars = ['damas', 'malibu', 'Traktor', 'Kamaz', 'spark']
# print(cars) #Tartiblanmagan holda
# cars.sort()
# print(cars) #Tartiblangan holda

# #Teskari holda
# cars = ['damas', 'malibu', 'traktor', 'kamaz', 'spark']
# print(cars) #Tartiblanmagan holda
# cars.sort(reverse=True)
# print(cars) #Tartiblangan holda

# cars = ['damas', 'malibu', 'traktor', 'kamaz', 'spark']
# print(cars) #Tartiblanmagan holda
# sorted(cars)
# print(cars) #Tartiblangan holda


# #Ruyxatni teskari chiqarish
# friends = ['Samandar', 'Javohir', 'Abdurahmon', 'Abdulaziz']
# friends.reverse()
# print(friends)
# print('Sizning ',len(friends),  'ta do`stingiz bor')


# # Range va Qadam

# sonlar = list(range(0, 10))
# print(sonlar)

# #JUFT VA TOQ SONLAR
# juft_sonlar = list(range(0,20,2))
# toq_sonlar = list(range(1,20,2))
# print(juft_sonlar)
# print(toq_sonlar)

# #MIN, MAX, SUM
# narxlar = [23409, 32487, 3278895, 84727542, 23547, 3528]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)

# print(f'Eng Arzon narx {arzon}, Eng qimmat narx {qimmat}, Jami: {jami}')

# #RUYXATNI KESISH
# mevalar = ['olma', 'anjir', 'shaftoli', 'o`rik', 'malena', 'olxo`ri', 'gilos']
# my_fruits = mevalar[1:3] # 2 dan 3 gacha elementlar chiqadi
# print(my_fruits)
# print(mevalar[2:5]) # 2-3-4 elementlar chiqadi
# print(mevalar[:4]) # Ruyxatdan boshidan 4 gacha kesadi
# print(mevalar[4:]) # 4 dan kyngi elementlarni chiqaradi


# #NUSXA OLISH
# mevalar = ['olma', 'anjir', 'shaftoli', 'o`rik', 'malena', 'olxo`ri', 'gilos']
# mevalar2 = mevalar[:] #Nusxalandi


# #TUPLES
# tomonlar = (20, 30, 55.5)
# print(tomonlar)

# toys = ['bus', 'car', 'bear', 'dino', 'snake', 'lizard']
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys[3] = 'dragon'

# print(toys)

# #TUPLES <->LIST
# toys = ['bus', 'car', 'bear', 'dino', 'snake', 'lizard'] # o`zgarmas ruyxat holati
# toys = list(toys) #Oddiy ruyxat holati
# #Ruyxatga uzgartirishlarni kiritamiz
# toys.append('fragon')
# toys.remove('bus')
# toys[1] = 'trian'
# toys = tuple(toys) # O`zgarmas ruyxat holati
# print(toys)