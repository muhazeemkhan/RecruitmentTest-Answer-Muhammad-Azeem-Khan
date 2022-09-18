class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        listA, listB = nums1, nums2;  # Assigning lists nums1, nums2 to 2 variables ListA and ListB respectively

        totalLength = len(listA) + len(listB);  # getting the total lenght of both lists
        halfLength = totalLength // 2;  # getting the half of total length of both the lists

        # we will make sure now that ListA is smaller than ListB otherwise we will swap them
        if len(ListA) > len(ListB):
            listA, listB = listB, listA;

        # creating left and right pointers that point to the start and the end of the list listA
        left, right = 0, len(listA) - 1;

        # now we are going to run a binary search on listA
        # This loop will continue to run until the if condition is fulfilled and if it doesnt it will continue to run other coniditions

        while True:
            i = (left + right) // 2;  # here we want the middle value of listA
            j = half - i - 2;  # here we want the middle value of listB. See here we cater for off by 1 since index start by 0

            # now we take the left an right values for both listA and listB respective to their partitions
            # we also have to cater for out of bound errors on both lists. So if its out of bound we give them value of -inf
            Aleft = listA[i] if i >= 0 else float("-infinity");
            Aright = listA[i + 1] if (i + 1) < len(listA) else float("infinity");

            Bleft = listB[j] if j >= 0 else float("-infinity");
            Bright = listB[j + 1] if (j + 1) < len(listA) else float("infinity");

            # Now we are going to apply the logic for this particular problem i.e if Aleft<=Bright and Bleft<=Aright
            if Aleft <= Bright and Bleft <= Aright:

                # checking if the total number of merged array in odd
                if totalLength % 2:
                    return min(Aright, Bright);

                # checking if the total number of merged array in even
                return max(Aleft, Bleft) + min(Aright + Bright) // 2

            # Now if the list listA is too big and the left of listA is greater than the right of listB
            elif Aleft > Bright:
                right = i - 1;  # We have reduced the size of the left partition of listA

            # Now for the case in which we have to increase the size of left partition of listA
            else:
                left = i + 1;




