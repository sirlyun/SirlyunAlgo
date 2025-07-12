from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def solution(numbers):
    """
    소수: 1과 본인 제외하고는 나눌 수 있는 숫자가 있으면 안됨
    :param numbers: 문자열로 주어지지만 각각의 숫자 표현
    :return: numbers의 숫자들로 만들 수 있는 소수의 개수
    """
    nums = list(numbers)
    result = set()

    for length in range(1, len(nums) + 1):
        for perm in permutations(nums, length):
            num = int(''.join(perm))
            result.add(num)

    answer = sum(1 for num in result if is_prime(num))

    return answer