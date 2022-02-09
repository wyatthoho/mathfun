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


def FindTickLR(tgt, aList) -> tuple:
    '''
    Find the values in aList which confine the value of tgt. For example,
    If aList = [1,2,3,4,5] and tgt = 3.5, then return (tickL, tickR) = (3, 4).
    '''
    tickL = aList[0]
    tickR = aList[-1]

    for tick in aList:
        if tick < tgt and tick > tickL:
            tickL = tick

        if tick > tgt and tick < tickR:
            tickR = tick
    
    return tickL, tickR


def PrintLoopState(msg, itr, total, inc=50):
    '''
    Use this function within a loop to print the status for the loop.
    '''
    if itr % inc == 0:
        print('\r{}: {}/{}'.format(msg, itr, total), end='', flush=True)
    elif itr == total:
        print('\r{}: {}/{}'.format(msg, itr, total), end='', flush=True)
        print('')