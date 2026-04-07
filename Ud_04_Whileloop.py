it = 5

while it > 1:
    print(it)
    it = it - 1
# While condition applay.
print ("while loop is executed")
#----------------------------------

it = 5

while it > 1:
    if it != 3:
        print(it)
    it = it - 1  #not equals to 3.
print("If statement is not equals to")
#------------------------------------------------

it = 10

while it > 1:
    if it == 3:
        break
    print(it)
    it = it - 1
print("break statement executed")

#Break statemet forces Early exit,improving efficiency and avoiding unnecessary iterations.
#------------------------------------------------

it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1
print("continue statement executed")


