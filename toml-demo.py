import toml

with open('pantry_data.toml', 'r') as file:
    file_data = toml.load(file)

# print(file_data)
# print(file_data['pantry']['dry_beans'])
rootKeys = list(file_data)
numKeys = len(rootKeys)
# Parse through the TOML file dictionary, break down the nested dictionary to get at each piece of data and get the properties
for x in range(numKeys-1):
    print(f"root key, {rootKeys[x+1]}")
    subKeys = list(file_data[rootKeys[x+1]])

    for y in range(len(subKeys)):
        print(f"\tsub key, {subKeys[y]}")
        subKeyData = list(file_data[rootKeys[x+1]][subKeys[y]])

        for z in range(len(subKeyData)):
            print(f"\t\t {subKeyData[z]}: {file_data[rootKeys[x+1]][subKeys[y]][subKeyData[z]]}")
            # [rootKeys[x + 1]][subKeys[y]][subKeyData[z]]
    print()


pantryKeys = list(file_data[rootKeys[1]])
closetKeys = list(file_data[rootKeys[2]])

print(f"{numKeys} The root keys are: {rootKeys}")
print(f"The pantry keys are: {pantryKeys}")
print(f"The closet keys are: {closetKeys}")