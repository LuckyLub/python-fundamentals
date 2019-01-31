'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?

print("Hello world"  --> SyntaxError: unexpected EOF while parsing
print("Hello world)  --> SyntaxError: EOL while scanning string literal



        * How helpful are the error messages?

pretty helpful, it points out where to look.

	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year.

'''

print("Hello world")
help('print')
print(3*3, 5%3, 8/7, 9//3)
print('Ammount of seconds in a year: ', 365*24*60*60)