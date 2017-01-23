import re

def RegularExpression():
    match = re.search('esh','Jayesh')
    print(match.group())

def Find(pattern, string):
    match = re.search(pattern,string)
    if match:
        print(match.group())
    else:
        print('match not found')

def main():
    #RegularExpression()
    Find('iig', 'piiglet')
    # . (dot) is any character
    Find('...sh','Jayesh')
    Find('..s.', 'Jayesh')
    # only find first occurence
    Find('..s.', 'Jayesh    oosp')

    # r makes raw string search and does not process '\' character separately
    # did not work though
    # Find(r'a\.e', 'Jayesh  ')

    # \w means word character
    # 3 chars after :
    Find(r':\w\w\w' , 'bleeh :dog haha')

    # \d is for digit
    Find(r'\d\d\d','blah blah 342xx-xxx')

    # \s is for white space
    Find(r'\d\s\d\s\d', 'blah blah 3 4 2xx-xxx')

    # + is for 1 or more
    Find(r'\d\s+\d\s+\d', 'blah blah 3     4                  2xx-xxx')

    # 1 or more word characters
    # \w does not accept & (only a-z,A-Z and 0-9 are accepted by \w)
    Find(r':\w+', 'blah blah :kitten123& blah blah')
    # 1 or more any character
    Find(r':.+', 'blah blah :kitten123& blah blah')
    # \S is for non white space (did not work with r (raw))
    Find(':\S+', 'blah blah :kitten123&Querystring1=qtr1&Quesrytring2=qtr2 blah blah')

    Find('\w+@\w+', 'blah jayesh.tambe@gmail.com blah @') # prints tambe@gmail.com not whole address

    # square bracket is set of characters you are looking for in pattern
    # [\w.] checks word character and normal '.'
    Find('[\w.]+@[\w.]+', 'blah jayesh.tambe@gmail.com blah @') #prints jayesh.tambe@gmail.com
    Find('[\w.]+@[\w.]+', 'blah .jayesh.tambe@gmail.com blah @')  # prints .jayesh.tambe@gmail.com
    Find('\w[\w.]+@[\w.]+', 'blah .jayesh.tambe@gmail.com blah @')  # prints jayesh.tambe@gmail.com, email must begin with word character

    match =  re.search('(\w[\w.]+)@([\w.]+)', 'blah .jayesh.tambe@gmail.com blah @')
    print('group 1 is ' + str(match.group(1)) + '\nand group 2 is ' + str(match.group(2)) )

    # gets all pattern matches in list
    print(re.findall('\w[\w.]+@[\w.]+', 'blah .jayesh.tambe@gmail.com blah @ another@alexa'))
    # prints ['jayesh.tambe@gmail.com', 'another@alexa']

    # gets all pattern matches in list of tuples
    print(re.findall('(\w[\w.]+)@([\w.]+)', 'blah .jayesh.tambe@gmail.com blah @ another@alexa'))
    # prints [('jayesh.tambe', 'gmail.com'), ('another', 'alexa')]

    print(re.findall('(\w[\w.]+)@([\w.]+)', 'blah .jayesh.tambe@gmail.com blah @ another@alexa', re.IGNORECASE))



if __name__ == '__main__':
    main()
