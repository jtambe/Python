
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

    #retuns a list of tuple
    print(dict.items())

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






def main():
    #dictionaryExercise()
    Cat(sys.argv[1])

if __name__ == '__main__':
    main()
