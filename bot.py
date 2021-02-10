import getopt, sys
import main
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[3:]
main.usr = sys.argv[1]
main.pwd = sys.argv[2]
options = "s:fc:h"
long_options = ["Story:", "Friend", "Comment:", "Help"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
    main.login()
    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print("Displaying Help")

        elif currentArgument in ("-s", "--Story"):
            main.story(currentValue)

        elif currentArgument in ("-c", "--Comment"):
            main.comment(currentValue)

        elif currentArgument in ("-f", "--Friend"):
            main.friendreq(0)

except getopt.error as err:
    main.driver.close()
    print(str(err))
