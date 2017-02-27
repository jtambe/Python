# str = "abcdef"
#
# for i in str:
#     print(i)
#
# i = 0
# while i < len(str):
#     print(str[i])
#     i += 1


#Dropbox Say what ypu see

def say_what_you_see(input_strings):
    if (len(input_strings) == 0):
        return False

    list = []

    for each in input_strings:
        i = 0
        result = ""

        if each == "":
            result.join("0")
        else:
            while i < (len(each)):
                current_val = each[i]
                count = 1
                while (i + 1 < len(each) and each[i + 1] == current_val):
                    i += 1
                    count += 1
                appendval = str(count) + str(current_val)
                result = result + appendval
                i += 1

        list.append(result)

    return list



inputList = ["215","5","0"]
inputList = ["12","21"]
inputList = ["05"]
inputList = ["2222","888888888"]
inputList = ["1111111111"]
inputList = ["112223"]

result = say_what_you_see(inputList)
print(result)


