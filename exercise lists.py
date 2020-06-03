numbers = [1, 5, 3, 6, 5, 4, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)