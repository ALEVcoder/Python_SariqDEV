# 11-Dars
# Sana: 22.08.2021
# Ko`chiruvchi: ALEVcoder


# ===================================================
# ===================================================
# MISOL

# yosh = int(input('Yoshingiz nechida? \n'))
# if yosh>=4:
#     print('Sizga kirish bepul')
# elif yosh<=12:
#     print('Sizga kirish 5000 so`m')
# elif yosh<=18:
#     print('Sizga kirish 8000 so`m')
# else:
#     print('Sizga kirish 10000 so`m')


# ===================================================
# ===================================================
# MISOL

# yosh = int(input('Yoshingiz nechida? \n'))

# if yosh>=4:
#     narh = 'bepul'
# elif yosh<=12:
#     narh = 5000
# elif yosh<=18:
#     narh = 8000
# else:
#     narh = 10000    

# print('Sizga kirish {narh} so`m')


# ===================================================
# ===================================================
# MISOL

# kun = input('Bugun nima kun ')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun Ish kuni')



# ===================================================
# ===================================================
# MISOL

# kun = input('Bugun nima kun ')
# if kun.lower() == 'shanba' and kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun Ish kuni')


# ===================================================
# ===================================================
# MISOL

# kun = input('Bugun nima kun ')
# harorat = float(input('Haroratni kiiritng '))
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and harorat >= 30:
#     print('Basseynga kettik')
# else:
#     print('Uyda Plasteshin o`ynaymiz')


# ===================================================
# ===================================================
# MISOL


# narx = 15000
# choy = True
# salat = True

# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000

# print(f'Jami {narx} so`m')


# ===================================================
# ===================================================
# MISOL


# narx = 15000
# choy = True
# salat = True
# non = True
# kompot = False
# limon_choy = False

# if choy:
#     print('Mijoz choy oldi.')
#     narx = narx + 3000
# if salat:
#     print('Mijoz salat oldi.')
#     narx = narx + 5000
# if non:
#     print('Mijoz non oldi.')
#     narx = narx + 6000
# if kompot:
#     print('Mijoz kompot oldi.')
#     narx = narx + 5000
# if limon_choy:
#     print('Mijoz limon choy oldi.')
#     narx = narx + 10000

# print(f'Jami {narx} so`m')


# ===================================================
# ===================================================
# MISOL


# menu = ['osh', 'somsa', 'kabob', 'norin', 'sho`rva', 'manti']
# ovqat = input('Nima ovqat yeysiz ')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi')
# else:
#     print(f'Keshirsiz bizda {ovqat} yuq')


# if ovqat.lower() not in menu:
#     print(f'Keshirsiz bizda {ovqat} yuq')
# else:
#     print('Buyurtma qabul qilindi')
    


# ===================================================
# ===================================================
# MISOL



menu = ['osh', 'somsa', 'kabob', 'norin', 'sho`rva', 'manti']
orders = ['osh', 'shashlik', 'norin', 'choy', 'pepsi']

for taom in orders:
    if taom in menu:
        print(f'{taom.title()} qabul qilindi.')
    else:
        print(f'Bizda {taom} yuq. Uzr')