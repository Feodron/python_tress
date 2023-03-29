per_1 = 1
per_2 = 2
per_3 = 3
new_per = per_1
per_1 = per_2
per_2 = new_per
new_new_per = per_2
per_2 = per_3
per_3 = new_new_per
print(per_1)
print(per_2)
print(per_3)