# a = [0, 1, 3, 0, 2] -> 0, 0, 1, 3, 2

# solution 1
a = [0, 1, 3, 0, 2]
x = []
y = []

for i in a:
    if i == 0:
        x.append(i)
    else:
        y.append(i)

print("solution 1", x+y)



# solution 2
a = [0, 1, 3, 0, 2]

zeros = a.count(0)
non_zero = [i for i in a if i !=0]

opt = [0] * zeros + non_zero
print("solution 2", opt)