# Task 1: Tuple Data Tipinə Element Əlavə Et (Başqa Data Tipindən Çevirərək)


# my_tuple = (1, 2, 3)
# element = "Salam"
# my_tuple = my_tuple + (element,)
# print("Task 1 Nəticəsi:", my_tuple)




# Task 2: Dict Üzərində Əməliyyatlar (Proqram Soruşsun, 1 - Keys, 2 - Values)
my_dict = {"ad": "John", "yaş": 30, "şəhər": "New York"}

while True:
    secim = input("Daxil edin 1 (Keys) və ya 2 (Values): ")
    
    if secim == "1":
        keys = my_dict.keys()
        for key in keys:
            print(key)
        break
    elif secim == "2":
        values = my_dict.values()
        for value in values:
            print(value)
        break
    else:
        print("Xəta! Yalnız 1 və ya 2 daxil edin.")


        

# Task 3: 2 Setin Ortasındakı Ortak Elementləri Tapmaq


# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# ortaq_elementlər = set1.intersection(set2)
# print("Task 3 Nəticəsi:", ortaq_elementlər)



# Task 4: Dict İçərisində Her birinin Dəyərləri int Olan 5 Keys və Values

# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# print("Task 4 Nəticəsi:", my_dict)
