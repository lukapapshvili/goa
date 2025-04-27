# 1) https://www.codewars.com/kata/57cff961eca260b71900008f
# def vowel_indices(word):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#     vowels_count = []

#     # Go through the letters word.
#     for index, letter in enumerate(word):
#         # Check if the letter is in vowels list of vowels uppercase list.
#         if letter in vowels or letter in [x.upper() for x in vowels]:
#             # Save the index of the letter.
#             vowels_count.append(index + 1)

#     return vowels_count
# 2) https://www.codewars.com/kata/58bf9bd943fadb2a980000a7
# def who_is_paying(name):
#     result = []
#     result.append(name)
#     if len(name) > 2:
#         result.append(name[0]+name[1])
#     return result
# 3) https://www.codewars.com/kata/55eea63119278d571d00006a
# def next_id(arr):
#     sorted_arr = sorted(arr)
#     sorted_arr = list(set(sorted_arr))
#     new_sorted_arr = []
#     for i in range(len(sorted_arr)):
#         if (sorted_arr[i] >= 0):
#             new_sorted_arr.append(sorted_arr[i])
#     for y in range(len(new_sorted_arr)):
#         if (new_sorted_arr[y] != y):
#             return y
#     return len(new_sorted_arr)