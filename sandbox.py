# a = "Welcome to Ops School, Winter 2020!"
#print(a[5])

#for i in a:
#    print(i)

#print("Welcome" in a)

import json

def sum_positive_numbers(num_list):
    """Sum all positive numbers in a list.

    Args:
        num_list: list of numbers to sum.

    Returns:
        integer sum of all positive numbers in the list.

    """
    sum = 0
    for index, num in enumerate(num_list):
        if num > 0:
            print(index)
            sum += num
    return sum

if __name__ == '__main__':
    #list_of_numbers = [12, 1, -7, 23, 80, 214, -9]
    #print(str(sum_positive_numbers(list_of_numbers)))
    # my_dict = {"name": "Arie", "age": 35}
    # print(my_dict["name"])
    # print(my_dict["age"])

    ppl_ages = {'david': 20, 'itzik': 30, 'yaron': 40}
    for name, age in ppl_ages.items():
        if age > 30:
            print("{} is older than 30".format(name))
        elif age == 30:
            print("{} is 30".format(name))
        else:
            print("{} is younger than 30".format(name))


    example = """{"name": "Nofar", "surname": "Spalter", "age": 37}"""
    json_parsed = json.loads(example)
    print(json_parsed["name"])

# print(name + " is older than 30")