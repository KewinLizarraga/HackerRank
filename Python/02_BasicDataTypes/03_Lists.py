"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands
where each command will be of the  types listed above. Iterate through each
command in order and perform the corresponding operation on your list.
"""

def commands(arg):
    list = []

    while arg > 0:
        i = input().split()

        if i[0] == "insert":
            list.insert(int(i[1]), int(i[2]))
        elif i[0] == "print":
            print(list)
        elif i[0] == "remove":
            list.remove(int(i[1]))
        elif i[0] == "append":
            list.append(int(i[1]))
        elif i[0] == "sort":
            list.sort()
        elif i[0] == "pop":
            list.pop()
        elif i[0] == "reverse":
            list.reverse()

        arg-=1

if __name__=="__main__":
    n = int(input())

    commands(n)
