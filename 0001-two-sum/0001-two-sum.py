# class Solution:
#     # [2,7,11,15]
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for keyI, valueI in enumerate(nums):
        #     # print("outer", keyI, valueI)
        #     for keyJ, valueJ in enumerate(nums[keyI+1:]): # [7,11,15]
        #         # print("inner", keyJ, valueJ)
        #         if valueI + valueJ != target:
        #             continue
        #         return [keyI, keyI+1+keyJ]
                    
        # return []



class Solution:
    # [2,7,11,15]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # print(n)
        for i in range(n):  # (0,1,2,3)
            # print(i, nums[i], range(i+1, n))
            for j in range(i+1, n):
                # print(j, nums[j])
                if nums[i] + nums[j] == target:
                    return[i, j]

        return []
