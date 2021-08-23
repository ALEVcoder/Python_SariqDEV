# 15-Dars | Practice
# Sana: 23.08.2021
# Ko`chiruvchi: ALEVcoder

python_words = {
    'integer':'Butun son',
    'float': "O'nlik son",
    'boolean':"Mantiqiy qiymat",
    'for':"Biror amalni qayta-qayta bajarish tsikli",
    'if':'Shartlarni tekshirish operatori'}

for key, value in sorted(python_words.items()):
    print(f"{key.title()} - {value}")



davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.upper())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")








menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")

    

