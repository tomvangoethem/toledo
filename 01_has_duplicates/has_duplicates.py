"""
Below you find five different versions of an algorithm that checks whether a list contains duplicates.
Analyze their time complexity for both the best and worst cases, and perform measurements to check your answer.

Also, compare the worst cases of version 1 and 2; what do you expect? Do your measurements confirm this?
"""
def has_duplicates_v1(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                return True
    return False

###############################################################################


def has_duplicates_v2(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False


###############################################################################


def has_duplicates_v3(lst):
    found_duplicate = False
    i = 0
    while i != len(lst):
        if lst.count(lst[i]) > 1:
            found_duplicate = True
        i += 1
    return found_duplicate


###############################################################################


def has_duplicates_v4(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            return True
    return False


###############################################################################


def has_duplicates_v5(lst):
    already_seen = {}
    for x in lst:
        if x in already_seen:
            return True
        already_seen[x] = True
    return False
