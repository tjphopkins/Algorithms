import random

def quick_sort(array):
    quick_sort_recursor(array, 0, len(array))  # right boundary is index of
                                                # last element + 1
    return array

def quick_sort_recursor(array, left_boundary, right_boundary):
    """
    Chooses and sorts a pivot element via the partition sub_routine, then makes
    recursive calls to sort the array either side of the sorted pivot element.

    left_boundary is the index of the first element,
    right boundary is the index of the last element + 1.
    """
    if left_boundary < right_boundary:
        split_point = partition(array, left_boundary, right_boundary)
        # recurse on either side of the split point
        quick_sort_recursor(array, left_boundary, split_point - 1)
        quick_sort_recursor(array, split_point, right_boundary)


def _choose_pivot(array, left_boundary, right_boundary):
    """Randomy selects an element from a given array to be the pivot. Swaps
    the pivot with the first element in the array.

    Modifies the array in place.
    """
    pivot_index = random.randint(left_boundary, right_boundary - 1)
    array[left_boundary], array[pivot_index] = array[pivot_index], array[left_boundary]
    return array[pivot_index]


def partition(array, left_boundary, right_boundary):
    """This is the partition sub-routine.

    sub_array is the subset of array between array[left_boundary] and
    array[right_boundary]

    modifies array in place

    returns the split point - that is, the position in the array where the
    pivot belongs, used to divide the list for recursive calls
    """
    _choose_pivot(array, left_boundary, right_boundary)
    pivot = array[left_boundary] _choose_pivot(array, left_boundary, right_boundary)
    i_index = left_boundary + 1
    for j_index in range(i_index, right_boundary):  # up to index of
                                                    # last element
        if array[j_index] < pivot:
            array[j_index], array[i_index] = array[i_index], array[j_index]
            j_index
            i_index += 1
    array[left_boundary], array[i_index - 1] = \
        array[i_index - 1], array[left_boundary]

    split_point = i_index

    return split_point
