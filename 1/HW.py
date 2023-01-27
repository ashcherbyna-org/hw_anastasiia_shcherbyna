def string_to_upper(string):
    return string.upper()


def mapping_str(strings):
    return map(string_to_upper, strings)


names = mapping_str(('alfred', 'ben', 'william'))

for name in names:
    print(name)


def float_to_second_pow(number):
    second_power = number ** 2
    return round(second_power, 3)


def number_for_pow(floats):
    return map(float_to_second_pow, floats)


powered_numbers = number_for_pow((4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59))

for power in powered_numbers:
    print(power)


def pairwise(list1, list2):
    return zip(list1, list2)


result = pairwise(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5])
print(tuple(result))


def select_str_of_len(list_str, number):
    def is_srt_of_len(strings):
        if len(strings) == number:
            return True
        return False

    return filter(is_srt_of_len, list_str)


strings_for_filter = ["Jeff", "Alex", "Jonathan", "Richelle", "Anna"]

filter_in_str = select_str_of_len(strings_for_filter, 4)
for results in filter_in_str:
    print(results)
