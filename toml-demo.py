import toml

with open('pantry_data.toml', 'r') as file:
    file_data = toml.load(file)

print(file_data)
print(file_data['pantry']['dry_beans'])