import timeit
import time
import requests
import math
import numpy


# def is_odd(number):
#     return number % 2 == 1

# def is_odd(number):
#
#     while number > 1:
#         number -= 2
#
#     if number == 1:
#         return True
#     else:
#         return False

# def is_odd(number):
#     binary_number = bin(number)
#     lsb = binary_number[-1]
#
#     return lsb == "1"

# def is_odd(number):
#     incrementor = 1
#     is_incrementor_odd = True
#     while incrementor < number:
#         incrementor += 1
#         if is_incrementor_odd:
#             is_incrementor_odd = False
#         else:
#             is_incrementor_odd = True
#
#     return is_incrementor_odd

# def is_odd(number):
#     is_odd_file = open('odd_numbers', 'r')
#     lines = is_odd_file.readlines()
#
#     for line in lines:
#         if str(number) == line.rstrip('\n'):
#             return True
#
#     return False

# def is_odd(number):
#     start = time.time()
#     x = 0
#     for i in range(2, number):
#         x += i % 2
#         time.sleep(0.01)
#     # print(f"Execution time: {time.time() - start:.2f} seconds")
#     return bool(x % 2)

# def is_odd(number):
#     api_url = "https://************/isodd/" + str(number)
#     response = requests.get(api_url)
#     response_json = response.json()
#
#     return response_json.get('isOdd')


# def is_odd(number):
#     # credit to u/ECC314
#     print(number)
#     print("shifted")
#     print(number << 31)
#     n = numpy.int32(number)
#     if n == 1 or n == 0:
#         print("A")
#         return True if n % 2 != 0 else False
#     if n << 31 == -1 and is_odd(n - 1) >= 0:
#         print("B")
#         return False
#     elif (n << 31) % 2 == 0 and is_odd(n - 1) % 2 == ((n - 1) << 31):
#         print("C")
#         return True
def is_odd(number):
    def is_palindrome(s):
        return s == s[::-1]

    if number == 1:
        return True

    string = ''
    last_was_left_par = False
    for x in range(1, number + 1):
        if last_was_left_par:
            string += '('
            last_was_left_par = False
        else:
            last_was_left_par = True
            string += ')'

    return is_palindrome(string)

# def is_odd(number):
#     # credit to u/evinrows
#     try:
#         exec('(' * len(range(number)[:math.floor(((number + 1)/2))]) + len(range(number)[math.floor(((number + 1)/2)):]) * ')')
#         return False
#     except Exception as e:
#         return True

def run_test(number):
    starttime = timeit.default_timer()
    result = is_odd(number)
    # print(result)
    endtime = timeit.default_timer() - starttime

    return endtime


if __name__ == "__main__":
    number_of_tests = 10000
    elapsed_time = 0
    print("==========================================")
    print("Intializing test for palindrome implementation")
    print("Number of trials: " + str(number_of_tests))
    print("==========================================")
    for x in range(1, number_of_tests + 1):
        elapsed_time += run_test(x)

    print("Average elapsed time is: " + str(elapsed_time / number_of_tests))

# base, API, ChatCPT answer, file read, reddit suggestions, if zero or 1, binary conversion,
