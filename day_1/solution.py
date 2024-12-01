with open("input_day_1.txt", "r") as data:

    list1 = []
    list2 = []
    distance = 0

    for line in data:
        numbers = line.strip().split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

    list1.sort()
    list2.sort()

    # Part 1
    for num1, num2 in zip(list1, list2):
        distance_each_number = abs(num1 - num2)
        distance += distance_each_number

    # Part 2
    similarity_score = 0
    for num in list1:
        similarity_score += num * list2.count(num)

print(distance)
print(similarity_score)


    