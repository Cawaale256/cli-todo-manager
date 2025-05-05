def merge_sort(task_list, attribute):
    if not task_list or not task_list.next:
        return task_list

    mid = get_middle(task_list)
    next_to_mid = mid.next
    mid.next = None

    left = merge_sort(task_list, attribute)
    right = merge_sort(next_to_mid, attribute)

    return sorted_merge(left, right, attribute)

def sorted_merge(left, right, attribute):
    if not left:
        return right
    if not right:
        return left

    if getattr(left, attribute) <= getattr(right, attribute):
        result = left
        result.next = sorted_merge(left.next, right, attribute)
    else:
        result = right
        result.next = sorted_merge(left, right.next, attribute)

    return result

def get_middle(node):
    slow = node
    fast = node
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
