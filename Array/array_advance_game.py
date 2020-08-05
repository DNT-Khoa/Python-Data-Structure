"""
You are given an array of non-negative integers. For example:
    [3, 3, 1, 0, 2, 0, 1]

Each number represents the maximum you can advance in the array

Question:
    Is it possible to advanced from the start of the array to the last element ?
"""


def array_advance(A):
    furthest_reached = 0
    last_index = len(A) - 1
    i = 0

    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(A[i] + i, furthest_reached)
        i += 1

    return furthest_reached >= last_index


A1 = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A1))

A2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A2))


# Explanation:

# There are two requirements to make sure we can reach the ene of the array:
# 1. A particular index (except for the first index) in the array should at least be reachable
# by its preceding number(s)
# 2. There must be a position from which we can reach the last index

# To satisfy the first requirement. The condition i <= furthest reached is to
# satisfy this task

# If i (current index) is larger than the furthest reached, it means that after checking the
# furthest index the preceding numbers can reach is less than the current index. As the same token,
# we can conclude that it cannot reach the last index in the array

# After we make sure that the current index can be reached. We continue to check if from that
# index we can proceed to the last index. If there is, we conclude that there is a position
# from which we can traverse to the end of the array
