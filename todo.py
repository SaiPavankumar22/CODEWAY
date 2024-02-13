work =[]

print("enter one of the option below")
print("1:-To add a new task")
print("2:-To delete a task")
print("3:-To display the list of tasks")
print("4:-Exit")
print("Enter your choice [1 or 2 or 3 or 4]")
k=int(input())
while (k!=4):
   k=int(input("re enter your option: "))
   if (k == 1):
       p=input("Enter the task details: ")
       work.append(p)
       print("Task is successfully added")
   elif (k == 2):
       p = input("Enter a task to remove: ")
       if (p in work):
           work.remove(p)
           print("The task is removed")
       else:
           print("The task is not present")
   elif (k == 3):
       print("Displaying the list of tasks")
       if(len(work)>0):
           for x in range(len(work)):
              print(work[x])
       else:
           print("There are no tasks present")
   elif (k == 4):
       print("Exiting the to do list")
       breakpoint
   else:
       print("Invalid option choosen")
