import sys


class InputValidator:

    def moduleUsageMessage(self, arg):
        '''Prints the usage message'''

        print("Usage: python %s <flag> <path>" % (arg))
        print("where:")
        print("\t<flag> = A flag(0 or 1) that tells whether to process a single input file(0) or a directory containing many files(1).")
        print("\t<path> = Path of the input file or the directory.")

    def checkFlagValidity(self, arg, flag):
        '''Validates the flag input'''

        if(flag != 0 and flag != 1):
            print("The input flag value is not valid.\n")
            self.moduleUsageMessage(arg)
            sys.exit(-1)  # Exit the program, in case of incorrect flag
