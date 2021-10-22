class Solution:
    def frequencySort(self, s: str) -> str:
        answer_ = {}
        for i in range(len(s)):
            if s[i] in answer_:
                answer_[s[i]] = answer_[s[i]] +1
            else:
                answer_[s[i]] = 1
        
        answer_list = sorted(answer_, key = lambda x:answer_[x], reverse = True  )
        result_ = ''
        
        for i in range(0,len(answer_list)):
            result_ = result_ + answer_list[i] * answer_[answer_list[i]]
        return result_
    
def main():
    string_input = str(input('Enter a string:'))
    string_input = string_input.replace(" ", "")
    solution  =  Solution()
    result = solution.frequencySort(string_input)
    print(result)

main()