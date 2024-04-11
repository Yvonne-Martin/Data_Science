#creating a stack
originalStack=[]
originalStack.append("Yvonne")
originalStack.append("Leila")
originalStack.append("Martin")
originalStack.append("Josphine")
print(originalStack)#output:['Yvonne', 'Leila', 'Martin', 'Josphine']

#removing an item in a stack
newStack=originalStack.pop(0)
print(newStack)#output:Yvonne

#adding an item in a stack
stack=originalStack.append("Kenya")
print(stack)
print(originalStack)#output:['Leila', 'Martin', 'Josphine', 'Kenya']


#accessing an item in  a stack
stack2=originalStack[2]
print(stack2)#output:Josphine


