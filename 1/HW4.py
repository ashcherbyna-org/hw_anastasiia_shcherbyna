#ex1
lst1 = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

lst2 = [i for i in lst1 if i < 21 or i > 74]
for num in lst2:
    lst1.remove(num)

print(lst1)

#ex2

store_dict = { "cito": 47.999,
               "BB_studio": 42.999,
               "momo": 49.999,
               "main-service": 37.245,
               "buy.now": 38.324,
               "x-store": 37.166,
               "the_partner": 38.988,
               "store": 37.720,
               "rozetka": 38.003
}
lower_limit = 35.9
upper_limit = 37.339

for key, value in store_dict.items():
    if lower_limit <= value <= upper_limit:
        print(key)


