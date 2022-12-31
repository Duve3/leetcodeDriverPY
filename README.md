# leetcodeDriverPY
A simple driver to allow you to use testcases in your own code :)

If you would like to use this in your project, its a simple as
just doing ```pip install leetcodeDriverPY```

Then once you have done that inside of your python file you will
want to do something like this:

###### top of the file:
```py
from leetcodeDriverPY import driver
```
###### inbetween these two segments of code should be your solution class with the solution function inside.
```py
sol = Solution()  # this should be your solution class
testcases = {  # create by doing: 'testcase': answer
    'answer': 'correct_solution',
}
driver(sol, testcases)
# ^ sol should be your Solution class
# testcases should be the testcases that you want to use to test your program.
```
###### If you class has more than one function inside you may run into issues, for that reason I added a "optionalFunc" parameter.
###### This would be how you use it:
```py
# this code is just the code from above but changed to use optionalFunc
sol = Solution()  # this should be your solution class
testcases = {  # create by doing: 'testcase': answer
    'answer': 'correct_solution',
}
driver(sol, testcases, optionalFunc=sol.IntToRoman)
# ^ optionalFunc should be your function REFERENCE! (ex: sol.IntToRoman)
# You shouldn't actually call the function.
```