
def balancedBrackets(n):
    return helper(0,n)


def helper(unmatched, toMatch):
    if toMatch == 0:
        return [""]

    result = []
    if unmatched < toMatch:
        tails = helper(unmatched+1, toMatch)
        result.extend( "(" + tail   for tail in tails )
    if unmatched > 0:
        tails = helper(unmatched - 1, toMatch -1)
        result.extend(")"+ tail  for tail in tails)

    return result



if __name__ == "__main__":
    print(balancedBrackets(3))
    # for i in range(4):
    #     print(balancedBrackets(i))




# Dangerous code
# str = ['1','2','3']
# str.extend(each + 'x' for each in str)
# print(str)




# Following Gayle's approach failed
# import numpy as np
#
# def getCombinations(left, right, parenthesisList, count):
#
#     if left < 0 or right < left:
#         return
#
#     if left == 0 and right == 0:
#         print(parenthesisList)
#     else:
#         if left > 0:
#             parenthesisList = parenthesisList + "("
#             getCombinations(left - 1 , right , parenthesisList, count + 1)
#         if right > left:
#             parenthesisList = parenthesisList + ")"
#             getCombinations(left , right - 1 , parenthesisList, count + 1)
#
#
# noOfPairs = 3
# parenthesisList = ""
# # print(parenthesisList)
#
# getCombinations(noOfPairs, noOfPairs, parenthesisList, 0)


#This is some 3rd approach I had come across, does not work
# def Brackets(output , open, close, pairs):
#     if open == pairs and close == pairs:
#         print(output)
#
#     else:
#         if open < pairs:
#             output = output+ "("
#             Brackets(output, open+1, close, pairs)
#         if close < open:
#             output = output + ")"
#             Brackets(output, open, close+1, pairs)
#
#     print(output)
#
# def Brackets2(n):
#     for i in range(1,n):
#         # print(i, end=" , ")
#         Brackets("",0,0,i)
#
# Brackets2(3)
