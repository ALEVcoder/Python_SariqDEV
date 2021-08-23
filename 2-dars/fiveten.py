# 15-Dars
# Sana: 23.08.2021
# Ko`chiruvchi: ALEVcoder

talaba = {
    'ism': 'alijon',
    'familya': 'valiyev',
    'yosh': 17,
    'fakultet': 'informatika',
    'kurs': 2
}

# print(talaba.items())

# for kalit, qiymat  in talaba.items():
#     print(f'Kalit: {kalit.title()}')
#     print(f'Qiymat: {qiymat} \n')


telphonelar = {
    'ali': 'iphone x',
    'vali': 'redmi note 10',
    'alijon': 'redmi note 9s',
    'samandar': 'samsung s21 ultra'
}
# for k, q in telphonelar.items():
#     print(f'{k.title()}ning telephni {q.title()}')


mahsulotlar = {
    'olma' : 10000,
    'banan' : 20000,
    'anor' : 15000,
    'anjir' : 25000,
    'shaftoli' : 17000
}
# print(mahsulotlar.keys())
# print(mahsulotlar.values())

# print("Do`kondagi mahsulotlar")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title()) 

bozorliklar = {
    'anor',
    'uzum',
    'non',
    'anjir',
    'baliq'
}

# for mahsulot in mahsulotlar:
#     if mahsulot in bozorliklar:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so`m")

# for buyum in bozorliklar:
#     if buyum not in mahsulotlar:
#         print(f'Iltimos, do`konga {buyum}ni ham olib keling')

# print('Do`konimizdagi mahsulotlar: ')
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# print(telphonelar.values())

# print('Foydalanuvchilar quyidagi telphonlarni ishlatadi:')
# for tel in telphonelar.values():
#     print(tel.title())



telphonelar = {
    'ali': 'iphone x',
    'vali': 'redmi note 10',
    'alijon': 'redmi note 9s',
    'alijon': 'redmi note 9s',
    'alijon': 'redmi note 9s',
    'samandar': 'samsung s21 ultra'
}

# print('Foydalanuvchilar quyidagi telphonlarni ishlatadi:')
# for tel in set(telphonelar.values()):
#     print(tel.title())

toys = {
    'ball',
    'car',
    'lamp',
    'ball'
}

print(toys)