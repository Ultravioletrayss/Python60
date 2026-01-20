def sum_of_dict_values(dict1):


    return sum(dict1.values())


def sum_of_dict_values1(dict1):
    total = 0
    for value in dict1.values():
        total += value
    return total

example_dict={"a":100,"b":200,"c":300}
print(sum_of_dict_values(example_dict))
print(sum_of_dict_values1(example_dict))