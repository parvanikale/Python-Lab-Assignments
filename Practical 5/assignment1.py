# Take input from user
nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# Total number of items
print("Total items:", len(nums))

# Last item
print("Last item:", nums[-1])

# Reverse order
print("Reversed tuple:", nums[::-1])

# Check if 5 is present
if 5 in nums:
    print("Yes")
else:
    print("No")

# Remove first and last item, sort remaining
new_tuple = nums[1:-1]   # removes first and last
sorted_tuple = tuple(sorted(new_tuple))

print("After removing first & last and sorting:", sorted_tuple)