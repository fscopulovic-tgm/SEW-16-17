def partition(lst):
    """
    Method idea from http://stackoverflow.com/questions/2659900/python-slicing-a-list-into-n-nearly-equal-length-partitions
    :param lst:
    :return [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(3)]: return a list, that has lists in it, those lists are seperated in the number what division got
    """
    div_three = len(lst) / 3
    return [lst[int(round(div_three * i)): int(round(div_three * (i + 1)))] for i in range(3)]