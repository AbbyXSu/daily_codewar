# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# Examples:
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']
def solution(s):
    result=[]
    l=len(s)
    if l % 2 != 0:
        s+='_'
        l+=1
    for i in range (0, l, 2):
        result.append(s[i:(i+2)])
    return result

# list comp
def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

