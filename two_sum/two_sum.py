class Solution:
    def twoSum(self, nums, target):
        # Brute force solution
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        #Somewhat more efficient solution
        numbers = {}
        for i in range(0, len(nums)):
                numbers[nums[i]] = i
        
        for i in range(0, len(nums)):
            if (target - nums[i] in numbers) and (numbers[target - nums[i]] != i):
                return [i,numbers[target - nums[i]]]

def main():
    input_list = []
    n = int(input("Enter total number of list elements : "))
    for i in range(0, n):
        ele = int(input())
        input_list.append(ele) # adding the element
        
    print(input_list)


    number_input = int(input('Enter a sum number:'))
    solution  =  Solution()
    result = solution.twoSum(input_list,number_input)
    print(result) 

main()