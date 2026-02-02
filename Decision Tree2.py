# Dataset: (a1, a2, a3, class)
data = [
    (True,  "Hot",  "High",   "No"),
    (True,  "Hot",  "High",   "No"),
    (False, "Hot",  "High",   "Yes"),
    (False, "Cool", "Normal", "Yes"),
    (False, "Cool", "Normal", "Yes"),
    (True,  "Cool", "High",   "No"),
    (True,  "Hot",  "High",   "No"),
    (True,  "Hot",  "Normal", "Yes"),
    (False, "Cool", "Normal", "Yes"),
    (False, "Cool", "High",   "Yes")
]

# Split data based on a1
true_branch = [row for row in data if row[0] == True]
false_branch = [row for row in data if row[0] == False]

# Check results for branches
false_result = set(row[3] for row in false_branch)

high_result = set(row[3] for row in true_branch if row[2] == "High")
normal_result = set(row[3] for row in true_branch if row[2] == "Normal")

# Print tree
print("Decision Tree\n")
print("          a1")
print("        /    \\")

print("     True    False")
print("      |        |")

print("     a3       ", list(false_result)[0])
print("   /    \\")

print("High  Normal")
print("  |      |")

print(high_result.pop(), "    ", normal_result.pop())
