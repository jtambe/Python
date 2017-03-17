
import sys

def dictionaryExercise():
    dict = {}
    dict['a'] = 'alpha'
    dict['b'] = 'beta'
    dict['o'] = 'omega'
    dict['g'] = 'gamma'

    print(dict['b'])

    # gives error
    #print(dict['x'])
    #work around, returns None
    print(dict.get('x'))

    # check if dictionary has key
    print('x' in dict)
    print('g' in dict)
    #does not work on values
    print('gamma' in dict)

    #return a list of keys
    print(dict.keys())
    print(dict.values())

    #print all data in sorted order
    for k in sorted(dict.keys()):
        print( k + ' -> ' + dict[k])

    for key,val in dict.items():
        print("key is: "+ key + " value : "+ val)

    #retuns a list of tuple
    print(dict.items())

    # just as good as iterating over a list of tupples
    for tupleItem in dict.items():
        print(tupleItem)



def Cat(filename):
    # r= reading , rU = takes care of dos/unix line endings

    # way #1
    f = open(filename, 'rU')
    # read each line
    # with this approach, should the file be very large, say 15 GB,
    # it does not require 15 GB of space to read file in memory. It reads one by one
    for line in f:
        #comma removes additional newline that print statement adds
        # did not work for windows command prompt
        print(line)
        #print(line,)

    #way #2
    # file needs to be opened every time  apparently
    f = open(filename, 'rU')
    # reads entire file as list of lines, which mean it will need 15 GB RAM
    lines = f.readlines()
    print(lines)

    #way #3
    f = open(filename, 'rU')
    # reads entire file as a string variable, which mean it will need 15 GB RAM
    fileText = f.read()
    print(fileText)



import collections
def dictionaryExercise2():
    mydict = {"jayesh":2, "zalex":1, "mili":23, "yuki":23, "xarin":11}
    print(mydict)
    #{'xarin': 11, 'yuki': 23, 'mili': 23, 'jayesh': 2, 'zalex': 1}

    # sorted(mydict, key = mydict.values())

    # print(sorted(mydict.items()))
    # sortedDict = sorted(mydict, key=mydict.__getitem__,mydict.values())
    # print(sortedDict)


    # sorted by values
    sortedMyDict = collections.OrderedDict( sorted(mydict.items(), key=lambda t:t[1], reverse=True) )
    print(sortedMyDict)
    #OrderedDict([('yuki', 23), ('mili', 23), ('xarin', 11), ('jayesh', 2), ('zalex', 1)])

    # sorted by keys
    sortedMyDict = collections.OrderedDict( sorted(sortedMyDict.items(), key=lambda t:t[0],reverse=True))
    print(sortedMyDict)
    # OrderedDict([('zalex', 1), ('yuki', 23), ('xarin', 11), ('mili', 23), ('jayesh', 2)])

    # following sorts dictionary by value first and then
    # that sorted dict of values is sorted for keys retaining order of values
    sortedMyDict = collections.OrderedDict(sorted(sortedMyDict.items(), key=lambda t:(t[1],t[0]), reverse= True ) )
    print(sortedMyDict)
    # OrderedDict([('yuki', 23), ('mili', 23), ('xarin', 11), ('jayesh', 2), ('zalex', 1)])

    for k,v in sortedMyDict.items():
        print(k, v)
    '''
    yuki
    23
    mili
    23
    xarin
    11
    jayesh
    2
    zalex
    1
    '''

    first = sortedMyDict.popitem(last=False)
    print(first)
    #('yuki', 23)



def dictionaryExercise3():


    dict = {}
    dict['k'] = 0
    print(dict)

    if 'k' in dict:
        dict['k'] = 5

    print(dict)


def SortingListOfDictionaries():

    # Note that list of dictionaries in here has same key value throughout

    persons =[{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}]
    newlist = sorted(persons, key=lambda k: k['name'])
    for i in range(len(newlist)):
        for k,v in newlist[i].items():
            print(str(k) + " : " + str(v), end="\n")

    from operator import itemgetter
    newlist = sorted(persons, key=itemgetter('name'))
    for i in range(len(newlist)):
        for k, v in newlist[i].items():
            print(str(k) + " : " + str(v), end="\n")

    newlist = sorted(persons, key=itemgetter('name'), reverse=True)
    for i in range(len(newlist)):
        for k, v in newlist[i].items():
            print(str(k) + " : " + str(v), end="\n")


def main():
    #dictionaryExercise()
    #Cat(sys.argv[1])
    #dictionaryExercise2()
    #dictionaryExercise3()
    SortingListOfDictionaries()


if __name__ == '__main__':
    main()
