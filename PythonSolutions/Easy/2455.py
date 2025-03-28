class Solution(object):
    def averageValue(self, nums):
        #Loop through the array and add the elements that are divisible by 3 to a temp
        temp = []
        for num in nums:

            if num%6 == 0: # Even numbers and divisible by 3 , if a number is a number is divisible by 6, it's even and divisible by 3 
                temp.append(num)

        avg = sum(temp)
        if avg != 0:
            return avg/len(temp)
        return 0