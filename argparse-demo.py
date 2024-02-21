import argparse

# use this to create an argparse object
parser = argparse.ArgumentParser()

# # use this method to add arguments, can also specify the type in here for if you want to work with numbers
# parser.add_argument("echo", help="echo the string used here")
# #  get the arguments entered by the user
# args = parser.parse_args()
# # in this case "echo" is the name of the command. so args.echo grabs the arguement entered in the position of the echo command's input
# print(args.echo)

# adding a -- to the argument makes it so that you have to provide a value after the command. To limit the values you
# can enter you can add in a "choices" and provide an array of acceptable values
# "default" lets you set what the value of the argument should be if no user input is given
# the "action" "store_true" allows you to simply enter the command and toggle a true/false, no need to add the value
# if you used the action="count" it would count the number of times the argument is entered
parser.add_argument("-s", "--silliness", help="increase output verbosity", action="store_true")
parser.add_argument("square", type=int, help="display a square of a given number")
args = parser.parse_args()
answer = args.square**2
# We have two arguments now, one is required. But its important to note that the order you enter them into the CLI doesn't matter
if args.silliness:
    print(f"silliness turned on, the square of {args.square} is {answer}")
else:
    print(answer)

