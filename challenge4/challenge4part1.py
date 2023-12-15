import random
c=random.randint(0,2)
if c%2==0:
    print("Heads")
else:
    print("Tails")
states_of_India=["Bihar","Delhi","WB"]
print(f" States {states_of_India[c]}")
names=["Bihar","Delhi","WB","NY"]

num_items=len(names)
billpay=random.randint(0,num_items-1)
print(f" The Bill will be paid by {names[billpay]}")

##coding challenge for treasure map
line1=["_","_","_"]
line2=["_","_","_"]
line3=["_","_","_"]
map=[line1,line2,line3]
print("Hiding your treasure: X marks the spot\n")
position=input()
map[int(position[0])-1][int(position[1])-1]="x"
print(f"{line1}\n{line2}\n{line3}")
