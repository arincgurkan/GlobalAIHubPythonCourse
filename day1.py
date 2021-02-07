#part1
list_swapped = [1,2,3,4,5,6,7,8,9,10,11]
list_swapped.reverse()
print(list_swapped)

#part2
nums = int(input("Enter a number: "))
#Increment nums by one because we need an inclusive range.
print([num for num in range(nums+1) if num%2 == 0])