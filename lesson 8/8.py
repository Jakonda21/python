def x(list):
    answer = 1
    for i in list:
        answer *= i
    return answer
print(x([1,2,3,4,5]))