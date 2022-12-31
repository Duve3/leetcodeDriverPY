class Colors:  # making it look colored
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class FunctionNotFound(BaseException):
    def __init__(self):
        print(f"{Colors.FAIL}Failed to find a function inside this class! Please enter a valid class.\nIf this class has more than 1 function, (excluding __ functions) then use the \"optionalFunc\" parameter.{Colors.ENDC}")  # NOQA:E501


def fillFunction():
    raise FunctionNotFound()


# simple driver that runs testcases
def driver(solution: type.__class__, testcases: dict, optionalFunc=None) -> None:
    if optionalFunc is None:
        functions = [attribute for attribute in dir(solution) if callable(getattr(solution, attribute)) and attribute.startswith('__') is False]
        if len(functions) == 1:
            func = eval(f"solution.{functions[0]}")
        else:
            func = fillFunction()
    else:
        func = optionalFunc
    numberCorrect = 0
    for testNum, testcase in enumerate(testcases):
        print("\n\n")
        print(f"Test {testNum + 1}/{len(testcases)}: {testcase}")
        val = func(testcase)  # NOQA:REF
        print(f"Test {testNum + 1}/{len(testcases)} returned: {val}.")
        if testcases[testcase] == val:
            print(f"{Colors.OKCYAN}Test {testNum + 1}/{len(testcases)} was SUCCESSFUL.{Colors.ENDC}")
            numberCorrect += 1
        else:
            print(f"{Colors.WARNING}Test {testNum + 1}/{len(testcases)} FAILED.{Colors.ENDC}")
    print(f"{Colors.BOLD}")
    if numberCorrect == len(testcases):
        print(f"{Colors.OKGREEN}\n\n*****\nALL SUCCESSFUL\n*****{Colors.ENDC}")
    elif numberCorrect > len(testcases) - 2:
        print(f"{Colors.WARNING}\n\n*****\n{numberCorrect}/{len(testcases)} Successful\n*****{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}\n\n*****\n{numberCorrect}/{len(testcases)} Successful\n*****{Colors.ENDC}")
