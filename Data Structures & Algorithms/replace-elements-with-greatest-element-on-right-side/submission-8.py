class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iterate in reverse building a newList
        # append curr_max to newList
        # compare curr with curr_max and update
        # repeat until end of array

        # iter both arr and newList (newList in reverse) and swap the values

        newList = []
        curr_max = -1

        # build newList
        for i in range(len(arr) - 1, -1, -1):
            newList.append(curr_max)
            curr_max = max(curr_max, arr[i])

        # iter both, and swap
        for i in range(0, len(arr)):
            arr[i] = newList[len(arr) - 1 - i]

        return arr
