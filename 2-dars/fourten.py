# 14-Dars
# Sana: 22.08.2021
# Ko`chiruvchi: ALEVcoder

# avto = {
#     'model': 'damas',
#     'rang': 'quymoq',
#     'narh': 20
# }
# print(avto['model'])
# print(avto['rang'], 'rang')
# print(avto['narh'],'$')

# mevalar = {
#     'olma': 10000,
#     'gilos': 5000,
#     'olcha': 15000
# }

# print(f"Gilosning narhi {mevalar['gilos']} so`m")


talaba = {
    'ism': 'abdulaziz ergashev',
    'yosh': 17,
    't_yil': 2004
}
print(f"{talaba['ism'].title()},\
    {talaba['yosh']} yoshda,\
    {talaba['t_yil']}-yilda tug`ulgan.")

print(f"{talaba['ism'].title()}, {talaba['yosh']} yoshda, {talaba['t_yil']}-yilda tug`ulgan.")

talaba['sinf'] = 11
talaba['qayerdan'] = 'samarqand'

print(f"{talaba['ism'].title()}, {talaba['yosh']} yoshda, {talaba['t_yil']}-yilda tug`ulgan, {talaba['sinf']}-sinf o`quvchisi, {talaba['qayerdan'].title()}da yashaydi.")


del talaba['yosh']

print(f"{talaba['ism'].title()}, {talaba['t_yil']}-yilda tug`ulgan, {talaba['sinf']}-sinf o`quvchisi, {talaba['qayerdan'].title()}da yashaydi.")


telphonelar = {
    'ali': 'iphone x',
    'vali': 'redmi note 10',
    'alijon': 'redmi note 9s',
    'samandar': 'samsung s21 ultra'
}

phone = telphonelar['samandar'].title()
print(f'Samandarning telphoni {phone}')

phone = telphonelar.get('samandar', 'Bunday ism yuq')
print(phone.title())

