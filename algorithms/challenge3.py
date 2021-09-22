# challenge 3

average_List = [23, 41, 90, 55, 71, 83]

def averageList(list):

    # for i in range(len(average_List)):
    #     average_List[i] += 3

    temp = [x+3 for x in list]
    sum = 0

    for i in range(len(temp)):
        sum += temp[i]

    # print(len(temp))
    return (sum/len(temp))

avg = averageList(average_List)
print(avg)