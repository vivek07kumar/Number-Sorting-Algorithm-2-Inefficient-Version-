# Removing Duplicates
    # 1. step 1 -: Take a number from user given list and place it in a new list.
    # 2. step 2 -: The take another number from user list and try matching its equality with elements of new list. If it matches then don't place it in new list. If it matches then place it in user list.
    # 3. Repeat the step 1 and step 2 until matching of all the numbers of user list is completed. New list will be the Non diplicate list.
# Finding Smallest to Greatest or vice versa
    # On every index you have to find the highest number on that list and exchange it with the number you were comparing with.
    # If you keep doing this for every index then the list will be sorted from Smallest to Greatest. Finding the Smallest number on each of the index will result in a list sorted from Greatest to Smallest.
def number_sorting(a) :
    n = len(a)
    i = 0
    while i < n :
        index_tracker = 0
        for x in a :
            if x > a[i] :
                a[i],a[index_tracker] = a[index_tracker],a[i]
            index_tracker = index_tracker + 1
        i = i + 1
    return a
def number_sorting_2(a) :
    n = len(a)
    i = 0
    while i < n :
        index_tracker = 0
        for x in a :
            if x < a[i] :
                a[i],a[index_tracker] = a[index_tracker],a[i]
            index_tracker = index_tracker + 1
        i = i + 1
    return a
def non_duplicate_list_function(user_list) :
    duplicate_list = user_list[:]
    non_duplicate_list = []
    duplicate_check = False
    duplicate_check_2 = True
    for variable_1 in duplicate_list :
        if non_duplicate_list == [] :
            non_duplicate_list = non_duplicate_list + [variable_1]
        else :
            for variable_2 in non_duplicate_list :
                if variable_1 != variable_2 :
                    duplicate_check = True
                else :
                    duplicate_check = False
                    duplicate_check_2 = False
        if duplicate_check and duplicate_check_2 :
            non_duplicate_list = non_duplicate_list + [variable_1]
        duplicate_check_2 = True
    return non_duplicate_list
def main() :
    user_input = eval(input('>>  Please enter numbers seperated by comma -: '))
    a = list(user_input)
    b = a[:]
    c = a[:]
    result = number_sorting(b)
    print()
    print('Smallest to Greatest ----> ',result)
    result_2 = number_sorting_2(c)
    print()
    print('Greatest to Smallest ----> ',result_2)
    result_3 = non_duplicate_list_function(result)
    print()
    print('After Removing Duplicate Number/s ---->  ',result_3)
    print('Number of Duplicate Element/s found ----> ',len(a) - len(result_3),'Element/s')
    print()
main()
