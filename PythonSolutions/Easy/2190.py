class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        ocur = {}
        for i in range(len(nums)-1):
            if nums[i] == key:
                next_num = nums[i+1]
                
                if next_num in ocur:
                    ocur[next_num] += 1
                else:
                    ocur[next_num] = 1

        mayor = 0
        resultado = None
        for num in ocur:
            if ocur[num] > mayor:
                mayor = ocur[num]
                resultado = num

        return resultado