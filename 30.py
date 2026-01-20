def remove_duplicates(lst):
    """
    Remove duplicates from a list.
    """
    return list(set(lst))
def remove_duplicates_with_order(lst):
    for i in range(0,len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                lst.pop(j)
    return lst

if __name__ == '__main__':
    lst=[10,20,30,10,20]
    print(remove_duplicates(lst))
    print(remove_duplicates_with_order(lst))