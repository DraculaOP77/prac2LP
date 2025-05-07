print("enter action to perform 1: additon 2:subtraction 3:multiplication 4:division")
action = int(input())
print("enter two numbers")
a = int(input())
b = int(input())

if action == 1:
    print("addition {}".format(a+b))
elif action == 2:
    print("subtraction {}".format(a-b))
elif action == 3:
    print("multiplication {}".format(a*b))
elif action == 4:
    print("division {}".format(a/b))

