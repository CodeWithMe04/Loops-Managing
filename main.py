# While Loops
count = 0
while count <= 10:
  print(count)
  count += 1

# For loops
for i in range(10):
  print(i)
  
# Lists
my_list = ["apple", "banana", "orange"]
print(my_list)

# Lists in loop
for x in my_list:
  print(x)

# Lists in loop with index
for i, x in enumerate(my_list):
  print(i, x)

#range in loops
for i in range(len(my_list)):
  print(i, my_list[i])

# Loops with if else statement
for x in my_list:
  if x == "banana":
    print("Found banana")
    break
  else:
    print("Not found")

# Break
for x in my_list:
  if x == "banana":
    print("Found banana")
    break

# Continue
for x in my_list:
  if x == "banana":
    continue
  print(x)
# While loop
count = 0
while count <= 10:
  print(count)
  count += 1

# 👋👋