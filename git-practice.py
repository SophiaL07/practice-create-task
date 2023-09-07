toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   toDoList.append(item)
   return toDoList

def deleteItem(item):
   toDoList.remove(item)
   return toDoList

userAns = input("Do you want to add to / remove from your list or quit? A/Q")
while userAns == "A":
   userAdd_Del = input("Do you want to add to or remove from your list? A/R")
   if userAdd_Del == "A":
      item = input("What item do you want to add?")
      addItem(item)
      userAns = input("Do you want to add to / remove from your list or quit? A/Q")
   else:
      item = input("What item would you like to remove?")
      if item not in toDoList:
         print("Error")
      else:
         deleteItem(item)
         userAns = input("Do you want to add to / remove from your list or quit? A/Q")