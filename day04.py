        # Day 04: Python Dictionaries (Ker-Value Pairs)
print("--- My Developer Profile ---")

# 1. Create a Dictionary

''' 
            dictionary_name = {
                        "key" : "value",
                        "key" : "value",
                        "key" : "value"
                    }

'''

developer = {
    "name":"Kavindu",
    "university":"OUSL",
    "target":"Software Engineering Internship",
    "Completed_days":3
}

# 2. Getting value using the related key
'''
           dictionary_name["key"] 
'''

print("developer Name:", developer["name"])
print("Current Target:", developer["target"])

print ("\n--- Updating Profile ---")

# 3. Adding and changing new things to the dictionary
"""
            Update -->  dictinary_name["key"] = new_value
            Add -->  dictinary_name["new_key"] = value
"""

developer["Completed_days"] = 4
developer["new_skill"] = "Python Dictionaries"

# 4. Passing a For Loop through a Dictionary

for key,value in developer.items():
    print(key + "-->" + str(value))