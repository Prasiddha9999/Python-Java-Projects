print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = "\tThe lovely world\
 with logic so firmly planted\
 cannot discern \n\t\t  the needs of love\
 nor comprehend passion from intuition\
 and requires an explantion\
\n\t\t\twhere there is none."

def print_heading(text, sep='-'):
    """
This function will print a nice heading.
    """
    print(sep * 15)
    print(text)
    print(sep * 15)

print_heading("Hello World")
print_heading(poem, sep='*')

def add_numbers(num1, num2):
    add = num1 + num2
    return add
add = add_numbers(num1=2, num2=3)
five = 10 - add
print("This should be five: {0}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return (int(jelly_beans), int(jars), int(crates))

start_point = 10000
bjc = secret_formula(start_point)
beans = bjc[0]
jars = bjc[1]
crates = bjc[2]

print("With a starting point of: {0}".format(start_point))
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have {0} beans, {1} jars, and {2} crabapples.".format(*secret_formula(start_point)))

sentence = "All good\tthings come to those who weight."
