p1 = "make a lot of memory"
p2 = "buy now"
p3 = "subscribs this"
p4 = "click this"

message = input("enter your comment:")

if((p1 in message)or(p2 in message)or(p3 in message) or(p4 in message)):
    print("this comment is a spam")
else:
    print("this comment is not spam")    