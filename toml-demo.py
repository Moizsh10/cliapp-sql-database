import toml

with open('pantry_data.toml', 'r') as file:
    file_data = toml.load(file)

# print(file_data)
# print(file_data['pantry']['dry_beans'])
rootKeys = list(file_data)
numKeys = len(rootKeys)
pantryKeys = list(file_data[rootKeys[1]])
closetKeys = list(file_data[rootKeys[2]])

print(f"{numKeys} The root keys are: {rootKeys}")
print(f"The pantry keys are: {pantryKeys}")
print(f"The closet keys are: {closetKeys}")