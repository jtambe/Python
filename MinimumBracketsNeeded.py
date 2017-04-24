'''
A string of brackets is correctly matched if you can pair every opening bracket up with a later closing bracket, and vice versa. For example, "(()())" is correctly matched, and "(()" and ")(" are not.

 Implement a function which takes a string of brackets and returns the minimum number of brackets you'd have to add to the string to make it correctly matched.

 For example, "(()" could be correctly matched by adding a single closing bracket at the end, so you'd return 1. ")(" can be correctly matched by adding an opening bracket at the start and a closing bracket at the end, so you'd return 2.

 If your string is already correctly matched, you can just return 0.

"(()())" = 0
"((())" = 1
"())" = 1
"()))" = 2

'''


def bracket_match(bracket_string):
    n = len(bracket_string)
    str = bracket_string
    stk = []
    i = 0
    count = 0
    while(i < n):
        if(str[i] == "("):
            stk.append(str[i])
        else:
            if( len(stk) >0 ):
                var = stk.pop()
            else:
                count += 1
        i += 1

    return max(len(stk), count)


print(bracket_match("(()())"))
print(bracket_match("((())"))
print(bracket_match("())"))
print(bracket_match("()))"))