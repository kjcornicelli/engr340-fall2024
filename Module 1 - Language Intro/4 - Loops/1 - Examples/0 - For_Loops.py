# Let's learn what a For Loop is!

# Lists are typically used to do certain operations
# over and over again. For the first example, we will
# go through a list and print out each number.

# The syntax for loops is like so: for "some variable" in
# "some range or container": do something.

list_one = [1, 2, 3, 4, 5]

for number in list_one:
    dummy = -1
    print(number)

# Notice how each number was printed in a new line? That shows
# that the operation happens once every "cycle" the program runs.

# Before your next run, comment out the above print statement, and
# uncomment the print statement below, that way the outputs make sense.

# This next loop shows how a range of numbers can be used for how many
# times a loop is run. In the bottom example, the loop will run 5 times.

for iteration in range(5):
    dummy = -1
    # print(iteration)

# Another common application for a for loop is to use the length of a list
# as the amount of times the loop runs. Same as before, comment out the
# previous print statement and uncomment the next print statement.

list_two = [5, 10, 15, 20, 25, 30]
list_two_looped = []

for number in range(len(list_two)):
    list_two_looped.append(list_two[number] - 5)
    # print(list_two_looped)

# As you can see, the "number" variable was used to represent the index of
# list_two, to be added to the previously empty list_two_looped! Notice how
# each print adds one more item to the new list.


# saving just in case

  a2 = (a1 + b1) / 2
    b2 = math.sqrt(a1 + b1)
    p2 = 2 * p1
    t2 = t1 - (p1 * ((a2 - a1) ** 2))

    a3 = (a2 + b2) / 2
    b3 = math.sqrt(a2 + b2)
    p3 = 2 * p2
    t3 = t2 - (p2 * ((a3 - a2) ** 2))

    a4 = (a3 + b3) / 2
    b4 = math.sqrt(a3 + b3)
    p4 = 2 * p3
    t4 = t3 - (p3 * ((a4 - a3) ** 2))

    a5 = (a4 + b4) / 2
    b5 = math.sqrt(a4 + b4)
    p5 = 2 * p4
    t5 = t4 - (p4 * ((a5 - a4) ** 2))

    a6 = (a5 + b5) / 2
    b6 = math.sqrt(a5 + b5)
    p6 = 2 * p5
    t6 = t5 - (p5 * ((a6 - a5) ** 2))

    a7 = (a6 + b6) / 2
    b7 = math.sqrt(a6 + b6)
    p7 = 2 * p6
    t7 = t6 - (p6 * ((a7 - a6) ** 2))

    a8 = (a7 + b7) / 2
    b8 = math.sqrt(a7 + b7)
    p8 = 2 * p7
    t8 = t7 - (p7 * ((a8 - a7) ** 2))

    a9 = (a8 + b8) / 2
    b9 = math.sqrt(a8 + b8)
    p9 = 2 * p8
    t9 = t8 - (p8 * ((a9 - a8) ** 2))