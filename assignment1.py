
def readAllData(filename):
    file = open(filename, 'r')
    l = []
    # print(file.readline())
    # print()
    # print(file.readlines())
    file.readline()

    for i in file.readlines():
        # print(i.split())
        # print(type(i))
        # tup = tuple(i.split())
        # print(tup)
        l.append(tuple(i.split()))
        # print(l)
    file.close()
    return l


def computeAverageForClasses(list_val):

    result = {}
    global set_lis
    set_lis = set()

    for i in list_val:
        set_lis.add(i[1])

    list_class = list(set_lis)
    number = list(i*0 for i in range(0, len(list_class)))
    total = list(i*0 for i in range(0, len(list_class)))

    for i in list_val:
        for j in range(0, len(list_class)):
            if i[1] == list_class[j]:
                total[j] += float(i[0])
                number[j] += 1

    for i in range(0, len(list_class)):
        result[list_class[i]] = total[i]/number[i]

    print(list_class)
    print(total)
    print(number)

    return result


def countMisclassified(avg_val, list_val):
    yes_avg = avg_val['YES']
    no_avg = avg_val['NO']

    list_class = list(set_lis)

    fo = open("Misclassified.txt", 'w')
    misclassified = 0

    for i in list_val:
        if i[1] == 'YES':
            if abs(float(i[0]) - yes_avg) > abs(float(i[0]) - no_avg):
                misclassified += 1
                fo.write(i[0])
                fo.write(", ")
                fo.write(i[1])
                fo.write('\n')
        else:
            if abs(float(i[0]) - no_avg) > abs(float(i[0]) - yes_avg):
                misclassified += 1
                fo.write(i[0])
                fo.write(", ")
                fo.write(i[1])
                fo.write('\n')

    fo.close()

    f = open("Misclassified_global.txt", 'w')
    misclassified_global = 0

    for i in list_val:
        for j in range(0, len(list_class)):
            if i[1] == list_class[j]:
                for k in range(0, len(list_class)):
                    if j != k:
                        if abs(float(i[0]) - avg_val[list_class[j]]) > abs(float(i[0]) - avg_val[list_class[k]]):
                            misclassified_global += 1
                            f.write(i[0])
                            f.write(", ")
                            f.write(i[1])
                            f.write('\n')

    f.close()
    # print(misclassified_global)
    # return misclassified_global
    return misclassified


list_data = readAllData('data.txt')
# print('List of tuple:')
# print(list_data)

avg_val = computeAverageForClasses(list_data)
print("Average Values of the classes in a dictionary: ", avg_val)

mis = countMisclassified(avg_val, list_data)
print("Total misclassified values in the file: ", mis)
