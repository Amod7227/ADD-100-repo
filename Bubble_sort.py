# Empty list for names
names = []

# Bubble sort to arrange letters alphabetically
def bubble_sort_alphabetical(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# User input
for i in range(5):
    user_name = input(f"Enter name {i + 1}: ")
    names.append(user_name)

# Sorted name list
bubble_sort_alphabetical(names)
print("Sorted list:", names)

# Reversed name list
names.reverse()
print("Reversed list:", names)