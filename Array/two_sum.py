# Given a sorted array of integers, return the two number such that 
# They add up to a specific target. You may assume that each input 
# would have exactly one solution, and you may not use the same element twice

A = [-2, 1, 2, 4, 7, 11]
target = 13

# Time complexity: O(n^2)
# Space complexity: O(1)
def two_sum_brute_force(A, target):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

# print(two_sum_brute_force(A, target))

# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]

    return False

# print(two_sum_hash_table(A, target))


# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(A, target):
    i = 0
    j = len(A) - 1

    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    
    return False

print(two_sum(A, target))
