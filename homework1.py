
def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path,'r',encoding='utf-8') as f:
            for line in f:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
        average = total/count
        return total,average
    except FileNotFoundError:
        print('File not found')
        return 0, 0
    except ValueError:
        print('File is damaged')
        return 0, 0
    except ZeroDivisionError:
        print ('File is empty')
        return 0, 0

total, average = total_salary('salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




def get_cats_info(path):
    try:
        with open(path,'r', encoding='utf-8') as f:
            cats = []
            for line in f:
                if not line.strip():
                    continue
                cat_id, name, age = line.strip().split(',')
                cat = {"id": cat_id, "name": name, "age": age}
                cats.append(cat)
        return cats
    except FileNotFoundError:
        print("File does not exist")
        return []


print(get_cats_info("cat_name.txt"))










