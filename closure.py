
#example 1
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        "Using nonlocal keyword value of paramter in enclosing scope is modified"
        #nonlocal number
        number=3
        print(number)
    printer()
    print(number)
# prints 3 9 without use of nonlocal
# prints 3 3 with use of nonlocal
print_msg(9)

#example 2
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter

# returns hex address of function data_transmitter
print(transmit_to_space("Test message"))

#example 3
def oneFunction(message):
	print(message)
oneFunction("One message")

def twoFunction(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter()
#prints additional 'None'
print(twoFunction("Two message"))

#example 4
def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter
#does not additional 'None' which is required behaviour
fun2 = transmit_to_space("Burn the Sun!")
fun2()

#example 5
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))

mutliplywith4 = multiplier_of(4)
print(mutliplywith4(9))