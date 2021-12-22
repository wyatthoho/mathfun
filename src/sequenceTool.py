"""
A Python module with functions to handle sequences.
"""


def CumulateList(alist) -> list:
    '''
    Return a cumulated list. For example,
    [1, 1, 1] -> [1, 2, 3]
    '''
    return [sum(alist[0:idx+1]) for idx in range(len(alist))]


def AvgSequence(sequence) -> float:
    '''
    Return the average of a sequence.
    '''
    num = 0
    total = 0
    for item in sequence:
        total += item
        num += 1

    return total/num

            
def GetIntersection(list1, list2) -> list:
    '''
    Get the intersected elements within two list.
    '''
    list3 = [value for value in list1 if value in list2]
    
    return list3

