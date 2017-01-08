import sys


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

def main():
    #print ("Hello")
    # print command line arguments
    print (sys.argv)
    # print what sys module contains
    print(dir(sys))
    # document page
    print(help(len))
    hello("jayesh")

if __name__ == '__main__':
    main()

