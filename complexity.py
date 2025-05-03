n = input("Enter a number: ")
n = int(n)
count = 0
for i in range(n):
    count +=1

print(f" n = {n}, Count = {count}")

# Time Complexity: O(n)
# Space Complexity: O(1)

n = input("Enter a number: ")
n = int(n)
count = 0
for i in range(n):      # O(n)
    count +=1              

for i in range(n):        # O(n^2)
    for j in range(n):
        count +=1

print(f" n = {n}, Count = {count}")

 # Time Complexity: O(n^2)
 # Space Complexity: O(1)
