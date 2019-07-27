# Program: Given Two strings, check to see if they are anagrams

arr1 = raw_input()
arr2 = raw_input()


def anagram(arr1, arr2):
    arr1 = arr1.replace(' ', '').lower()
    arr2 = arr2.replace(' ', '').lower()

    if len(arr1) != len(arr2):
        return False

    count = dict()

    for letter in arr1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in arr2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for key in count:
        if count[key] != 0:
            return False

    return True


print anagram(arr1, arr2)