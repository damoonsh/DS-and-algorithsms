def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i+1] = a_list[i+1],a_list[i]

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(a_list)
# print(a_list)

# This version will stop early given that the list is sorted
def short_bubble_sort(a_list):
    exchanges, pass_num = True, len(a_list) - 1

    while pass_num > 0 and exchanges:
        exchanges = False

        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i + 1], a_list[i] = a_list[i], a_list[i + 1]
        
        pass_num -= 1