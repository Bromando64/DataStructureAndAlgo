# log all pairs of array

boxes = [1, 2, 3, 4, 5]
new = []
for i in boxes:
    for j in boxes:
        tup = (i, j)
        if i != j:
            new.append(tup)

print(new)
