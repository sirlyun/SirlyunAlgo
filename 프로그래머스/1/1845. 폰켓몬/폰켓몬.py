def solution(nums):
    n = len(nums)
    max_selection = n // 2
    unique_kinds = len(set(nums))

    return min(max_selection, unique_kinds)