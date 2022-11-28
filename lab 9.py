###########################################
# EECS1015 - Practice Final Exam
# Fall 2022, York University
# Starting code
#
###########################################
import random

def student_info():
    print("Name: Ashley Pereira")
    print("Section B")
    print("Student id: 218681254")
    print("Email: ash03@my.yorku.ca")


def task0():
    student_info()


def yes_no(yn):
    yn = yn.upper()
    if (yn == "Y"):
        return True
    elif (yn == "N"):
        return False


def task1():
    removing_words = True
    while removing_words:
        sentence = input("Type in a long sentence: ").split()
        sentence_remove = input("Remove words containing: ")
        with_substr = ""
        without_substr = ""
        for i in sentence:
            if sentence_remove in i:
                with_substr += i + " "
        for i in sentence:
            if not sentence_remove in i:
                without_substr += i + " "
        print(f"With substring: {with_substr}")
        print(f"W/O  substring: {without_substr}")
        removing_words = yes_no(input("Try again? [Y/N] ")) 
    

# write randomlist and reshape for task2 below


def random_list(N):
    ran_list = []
    for i in range(N):
        ran_list.append(random.randint(0,9))
    return ran_list


def reshape(a_list, num_rows, num_cols):
    new_list = []
    a_list_size = len(a_list)
    for i in range(0, a_list_size, num_cols):
        new_list.append(a_list[i:i+num_cols])
    return new_list

def task2():
    list_reshaping = True
    while list_reshaping:
        num = int(input("List length: "))
        ran_list = random_list(num)
        print(ran_list)
        row_col = True
        while row_col:
            num_rows = int(input("Rows: "))
            num_cols = int(input("Cols: "))
            if num_rows * num_cols != num:
                print(f"Error: {num_rows}*{num_cols} != {num}")
            else:
                break
        reshape_list = reshape(ran_list, num_rows, num_cols)
        print("Reshaped List")
        print(reshape_list)
        list_reshaping = yes_no(input("Try again? [Y/N] "))


# write function find_duplicates() for task 3 below

def find_duplicates(a_dict):
    new_dict = {}
    final_dict = {}
    for key, value in a_dict.items():
        new_dict.setdefault(value, set()).add(key)
    for key, value in new_dict.items():
        if (len(value)!=1):
            final_dict[key]=value
    return final_dict


def task3():
    values_in_dict = True
    while values_in_dict:
        print("Input words, press enter to end.")
        dict = {}
        counter = 0
        while True:
            counter+= 1
            input_dict = input(f"[Input {counter:2}] Word: ")
            if (input_dict == ''):
                break
            dict[counter] = input_dict
        print("Dictionary")
        print(dict)
        duplicates = find_duplicates(dict)
        print("Duplicates")
        print(duplicates)
        values_in_dict = yes_no(input("Try again? [Y/N] ")) 

# write class rangeChecker for task4 below

class range_checker:

    range_counter = 1

    def __init__(self, name, min, max) -> None:
        assert max>min, f"Max ({max}) must be greater than min ({min})"
        
        self.id = range_checker.range_counter
        range_checker.range_counter += 1

        self.name = name
        self.min_value = float(min)
        self.max_value = float(max)

    
    def within_range(self, number):
        if (number < self.min_value) or (number > self.max_value):
            return True
        else:
            return False

    
    def outside_range(self, number):
        if (number < self.min_value) or (number > self.min_value):
            return True
        else:
            return False

    
    def print_fun(self):
        print(f'range_checker [{self.id:2}]   {self.name:10} {self.min_value:.2} <= num <= {self.max_value:.2}')


def task4():
    name0, min0, max0 = input("Range 0 Name, Min, Max: ").split(',')
    range0 = range_checker(name0, min0, max0)
    name1, min1, max1 = input("Range 1 Name, Min, Max: ").split(',')
    range1 = range_checker(name1, min1, max1)
    name2, min2, max2 = input("Range 2 Name, Min, Max: ").split(',')
    range2 = range_checker(name2, min2, max2)
    num_input = input("Input list of numbers x1, x2,..., xn: ").split(',')
    range_checker.print_fun(range0)
    range_checker.print_fun(range1)
    range_checker.print_fun(range2)

def main():
    task0()
    print("--- Task 1 ---")
    task1()
    print("\n--- Task 2 ---")
    task2()
    print("\n--- Task 3 ---")
    task3()
    print("\n--- Task 4 ---")
    task4()

if __name__ == "__main__":
    main()