class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = None, None
        count1, count2 = 0, 0

        # Step 2
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 3
        count1, count2 = 0, 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1

        # Step 4 and 5
        n = len(nums)
        res = []
        if count1 > n // 3:
            res.append(num1)
        if count2 > n // 3 and num2 != num1:
            res.append(num2)

        # Step 6
        return res