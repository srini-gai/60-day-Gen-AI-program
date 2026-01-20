task= ["eat", "code", "sleep"]

print(task) # Prints the initial list

task.append("Repeat") # Adds "Repeat" to the end of the list

print(task)

for i in task :
    print(i) # Prints each item in the list
    if i == "code" :
        print(f" - {i} ✅ Code is working")
        '''print("Code is Working") #  message when the item is "code" '''
    else:
        print(f"- {i} ✔ ok")     

task.reverse() # Reverses the list order

print(task) 

''' print("ok") # Prints "ok" for all other items '''