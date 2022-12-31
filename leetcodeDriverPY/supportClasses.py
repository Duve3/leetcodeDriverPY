class Colors:  # Colors required for making look **good**
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # in order to stop colors from filling the entire terminal.
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Custom function not found exception, used for missing functions
class FunctionNotFound(BaseException):
    def __init__(self, text=None):
        if text is None:
            print(f"{Colors.FAIL}ERR: Failed to find a function inside this class! Please enter a valid class.\nIf this class has more than 1 function, (excluding __ functions) then use the \"optionalFunc\" parameter.{Colors.ENDC}")  # NOQA:E501
        else:
            print(f"{Colors.FAIL}ERR: {text}{Colors.ENDC}")


# Custom Not Enough Testcases exception, used when len(testcases) == 0
class NotEnoughTestcases(BaseException):
    def __init__(self, text=None):
        if text is None:
            print(f"{Colors.FAIL}Testcases length is too small!{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}ERR: {text}{Colors.ENDC}")


def fillFunction():
    raise FunctionNotFound("We failed to find a function inside this class provided.\n"
                           "Please enter a valid class. If this class has more than ONE function inside "
                           "(excluding __ functions), then use the \"optionalFunc\" parameter to enter the function.")
