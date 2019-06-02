# Insertion sort (ascending)

# Input: int array, arr

# Time: O(n^2) -> in worst case (reverse order), must swap 
#                 1, 2, 3,... n-1 times = n(n-1)/2 times 
#                 ~= O(n^2)
# Space: O(1)  -> stable in-place sort

from typing import List

def sort(arr: List[int]):
    for i in range(1, len(arr)):
        curr = i
        if arr[curr] < arr[curr-1]:
            while arr[curr] < arr[curr-1] and curr > 0:
                arr[curr], arr[curr-1] = arr[curr-1], arr[curr]
                curr -= 1

if __name__ == "__main__":
    arr = [9, 4, 6, 1, 5, 2, 7, 8, 3]
    sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Yippeee insertion-sorted the arr {arr}")

    allZeroesArr = [0, 0, 0, 0]
    sort(allZeroesArr)
    assert allZeroesArr == [0, 0, 0, 0]
    print(f"Yippeee insertion-sorted the arr {allZeroesArr}")

    alreadyAscArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sort(alreadyAscArr)
    assert alreadyAscArr == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Yippeee insertion-sorted the arr {alreadyAscArr}")