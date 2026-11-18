from age import cat, cat_id

# with open('salary.txt', 'w', encoding='utf-8') as f:
#     f.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\n')
#
# def total_salary(path):
#     total = 0
#     count = 0
#     try:
#         with open(path,'r',encoding='utf-8') as f:
#             for line in f:
#                 name,salary = line.strip().split(',')
#                 total = total+ int(salary)
#                 count = count + 1
#         average = total/count
#         return total,average
#     except FileNotFoundError:
#         print('File not found')
#         return 0, 0
#     except ValueError:
#         print('File is damaged')
#         return 0, 0
#     except ZeroDivisionError:
#         print ('File is empty')
#         return 0, 0
#
# total, average = total_salary('salary.txt')
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



# with open('cat_name.txt', 'w', encoding='utf-8') as f:
#     f.writelines([
#         '60b90c1c13067a15887e1ae1,Tayson,3\n',
#         '60b90c2413067a15887e1ae2,Vika,1\n',
#         '60b90c2e13067a15887e1ae3,Barsik,2\n',
#         '60b90c3b13067a15887e1ae4,Simon,12\n',
#         '60b90c4613067a15887e1ae5,Tessi,5\n',
#     ])

# def get_cats_info(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as f:
#             cats = []
#             for line in f:
#                 if not line.strip():
#                     continue
#                 cat_id, name, age = line.strip().split(',')
#                 cat = {"id": cat_id, "name": name, "age": age}
#                 cats.append(cat)
#         return cats
#     except FileNotFoundError:
#         print("File does not exist")
#         return []
#
#
# print(get_cats_info("cat_name.txt"))










