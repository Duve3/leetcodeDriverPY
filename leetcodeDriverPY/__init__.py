from .supportClasses import ColorsClass, fillFunction, NotEnoughTestcases
Colors = ColorsClass()
version = '1.1.1'


# simple driver that runs testcases
def driver(sol: type.__class__, testcases: dict, optionalFunc=None, colorless=False) -> None:
    assert isinstance(testcases, dict), "testcases must be a dictionary that is setup like this: {testcase:answer}!"
    assert isinstance(sol, type.__class__), "solution must be the original class! Not an instance."
    solution = sol()

    if colorless:
        Colors.clear()
    if len(testcases) < 1:
        raise NotEnoughTestcases("testcases must contain at least one testcase!")
    if optionalFunc is None:
        functions = [attr for attr in dir(solution) if callable(getattr(solution, attr)) and attr.startswith('__') is False]  # NOQA:E501
        if len(functions) == 1:
            func = getattr(solution, functions[0])
        else:
            func = fillFunction()
    else:
        func = optionalFunc

    numberCorrect = 0
    print(f"leetcodeDriverPY v{version}")
    print(f"Using function: {solution.__class__.__name__}.{func.__name__}()")
    for testNum, testcase in enumerate(testcases):
        print(f"Test {testNum + 1}/{len(testcases)}: {testcase}")
        val = func(testcase)
        print(f"Test {testNum + 1}/{len(testcases)} returned: {val}.")
        if testcases[testcase] == val:
            print(f"{Colors.OKCYAN}Test {testNum + 1}/{len(testcases)} was SUCCESSFUL.{Colors.ENDC}")
            numberCorrect += 1
        else:
            print(f"{Colors.WARNING}Test {testNum + 1}/{len(testcases)} FAILED.{Colors.ENDC}")
        print("\n\n")

    if numberCorrect == len(testcases):
        print(f"{Colors.BOLD}{Colors.OKGREEN}\n\n*****\nALL SUCCESSFUL\n*****{Colors.ENDC}")
    elif numberCorrect > len(testcases) // 2:
        print(f"{Colors.BOLD}{Colors.WARNING}\n\n*****\n{numberCorrect}/{len(testcases)} Successful\n*****{Colors.ENDC}")
    else:
        print(f"{Colors.BOLD}{Colors.FAIL}\n\n*****\n{numberCorrect}/{len(testcases)} Successful\n*****{Colors.ENDC}")
