#accessing items in a tuple
person=("yvonne","martin","Lovelace")
print(person[2])

#adding items on a tuple
new_person=person + (23,)
print(new_person)#output:('yvonne', 'martin', 'Lovelace', 23)

#Removing items from tuple
remove = person[:1 ]+ person[2:]
print(remove)
print(person)#output:('yvonne', 'Lovelace')

