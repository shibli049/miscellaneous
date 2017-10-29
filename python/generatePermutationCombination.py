import itertools
myPerm = list(map(",".join, itertools.permutations(['I','We', 'You' , 'They'])))

print("combinations: ")
myComb = list(map(",".join, itertools.combinations(['I','We', 'You' , 'They'], 2)))
i = 1
for item in myComb:
    print( str(i) + "=" + str(item) )
    i = i + 1

print("\npermutations: ")
i = 1
for item in myPerm:
    print( str(i) + "=" + str(item) )
    i = i + 1

