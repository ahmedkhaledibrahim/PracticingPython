from sys import flags

from src.Animal import Animal
from src.Dog import Dog


def isValid(s):
    paranthees_dict = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
    result_list = []
    for parenthesis in s:
        if parenthesis in paranthees_dict:
            if len(result_list) == 0:
                return False
            else:
                last_element = result_list.pop()
                if last_element != paranthees_dict[parenthesis]:
                    return False
        else:
            result_list.append(parenthesis)
    if len(result_list) > 0:
        return False
    else:
        return True


# wrong
def strStr_wrong(haystack, needle):
        pt1 = 0
        pt2 = 0
        flag = -1
        match_counter = 0
        while pt2 < len(haystack):
            if haystack[pt2] == needle[pt1]:
                match_counter = match_counter+1
                if flag == -1:
                    flag = pt2
                if match_counter == len(needle):
                    return flag
                pt2 = pt2 + 1
                pt1 = pt1 + 1
            else:
                flag = -1
                pt2 = pt2 + 1
                pt1 = 0
        return -1


def strStr(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1



def findClosestNumber(nums):
    i = 0
    closestIndex = float('inf')
    while i < len(nums):
        if abs(nums[i]) - 0 < abs(closestIndex):
            closestIndex = nums[i]
        elif abs(nums[i]) - 0 == closestIndex:
            closestIndex = max(closestIndex,nums[i])
        i +=1
    return closestIndex

findClosestNumber([-10000,-10000])