# Can you compute all multiples of 3, and 5
# That are less than 100?

list_100 = list(range(1, 100))
list_multiples = []

for i in list_100:
    if i % 3 == 0 or i % 5 == 0:
        list_multiples.append(i)

print(list_multiples)
    