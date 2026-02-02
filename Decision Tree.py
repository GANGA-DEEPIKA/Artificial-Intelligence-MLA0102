data = [
    ("Sunny","High","No"),
    ("Sunny","Normal","No"),
    ("Overcast","High","Yes"),
    ("Rain","High","Yes"),
    ("Rain","Normal","Yes")
]

def decision_tree(outlook, humidity):
    if outlook == "Overcast":
        return "Yes"
    if outlook == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"
    if outlook == "Rain":
        return "Yes"

# Testing
correct = 0
for o,h,y in data:
    if decision_tree(o,h) == y:
        correct += 1

print("Accuracy:", correct/len(data))
