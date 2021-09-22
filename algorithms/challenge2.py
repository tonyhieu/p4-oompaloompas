# challenge 2

list1 = [5, 3, 4, 1, 2]

def orderList(list):

    temp = list # create copy of list
    result = []

    for j in range(len(temp)):  # find minimum x times and append to

        min = 99999999999

        for i in range(len(temp)):
            if temp[i] <= min:
                min = temp[i]
        result.append(min)
        # print(j)
        del temp[i]
        # print(temp)

    return result

list2 = orderList(list1)
print(list2)