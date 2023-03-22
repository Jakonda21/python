def xx(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(xx([1,2,3,4,5],[5,6,7,8,9]))
print(xx([1,2,3,4,5], [6,7,8,9]))