import sys
import itertools

def hello(name):
    if name == "jayesh" or name == 'jess':
        name = name + '??'
    else:
        name = name + '<<'
    name = name + '!!'
    # comma separates them with a space
    print("hello", name)
    print(name[:])
    print(name[2:])
    print(name[3:4])
    print(name[:4])

def pyStringOps():
    myString = "ABCDEFGHIJKLMNOP"
    print(myString.__contains__("ABC"))
    print(myString.__contains__("PQR"))

    print(myString.lower())
    print(myString.upper())
    print(myString[0])

    # slow way to manipulate string in python
    myStringList = list(myString)
    myStringList[0] = "X"
    myString = str("".join(myStringList))
    print(myString)

    print(myString[:-1])

    # faster way to manipulate string in python
    testString = myString[:1]+ 'NEW' + myString[2:]
    print(testString)

def pyTwoListsLoop():

    names = ['Jayesh', 'Alena', 'Milan', 'Amber']
    ids = [23,90]

    # zip uses itertools
    for x,y in zip(names,ids):
        print(str(y) + ' : ' + str(x) )

    # zip uses itertools
    for x, y in itertools.zip_longest(names, ids):
        print(str(y) + ' : ' + str(x))


    namesLength = len(names)
    idsLength = len(ids)
    for i in range(namesLength):
        print( str(names[i]) + ' - ' + str(ids[i%idsLength]) )



def pyLists():
    a = [1, 2, 'kill']
    # using str as only lists can be concatenated
    print(str(a) + ' ' + 'len(a): ' + str(len(a)) )
    # b and a point to same thing
    b = a
    # c is an independent copy
    c = a[:]

    c[1] = 'jol'
    if c == a:
        print('c and a are same lists')
    else:
        print('c and a are not same lists')

    #foreach
    for listItem in c:
        print(listItem)

    # checks if c contains 'kill'
    print(str('kill' in c))

    # append values to lists
    c.append('jason')
    c.append(45.9)
    print(c)

    #remove an element, removing 4th element
    c.pop(4)
    print(c)
    del c[3]
    print(c)

    #sorting list
    d = [3,67,23,1]
    e = ['jason', 'kill', 'ajax', 'cream','ball']
    print(sorted(d))
    print(sorted(e, reverse=True))
    e.sort()
    print(e)

def sortByLength():
    a = ['aa','qqqqq','ddd','eeee','bbbbbb']
    b = (sorted(a, key=len))
    print(a)
    print('sort by length of string')
    print(b)

def Last(s):
    return s[-1]

def sortByLastChar():
    a = ['aa', 'qqqqq', 'ddd', 'eeee', 'bbbbbb']
    print('sort by last character')
    print(sorted(a,key=Last))
    print('sort by last character in reverse')
    print(sorted(a, key=Last, reverse=True))

    #join all items in list
    print('\n'.join(a))
    print(':'.join(a))

    #use of split in a string
    b = '#'.join(a)
    print(b)
    print(b.split('#'))

    print('plain for loop')
    for i in range(4):
        print(i)

def tupleExercise():
    print('inside tuple')
    a = ('x', 'y', 'z')
    print(a)
    #list of tuples
    a = [(1,"b") ,(2,"a"), (1,"a")]
    print(a)
    print('sorting tuple')
    print(sorted(a))

def main():
    #print ("Hello")
    # print command line arguments
    #print (sys.argv)
    # print what sys module contains
    #print(dir(sys))
    # document page
    #print(help(len))
    #hello("jayesh")
    #pyLists()
    #pyStringOps()
    pyTwoListsLoop()
    #sortByLength()
    #sortByLastChar()
    #tupleExercise()

if __name__ == '__main__':
    main()

