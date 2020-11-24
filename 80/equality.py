from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    if list1 == list2:
        print(Equality(3))
        return Equality(3)


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4, 1]
    list3 = [1, 2 ,3, 4]
    list4 = [1, 1, 2, 3, 4]
    list5 = [5, 6, 7, 8]
    list6 = list1

    test = check_equality(list1, list3)


