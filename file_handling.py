file_path = "demo/input.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File {file_path} not found.")
except PermissionError:
    print(f"You do not have permission to read {file_path}.")

output_path = "demo/output.txt"

data_to_write = "Hello World!"

try:
    with open(file=output_path, mode="w") as file:
        file.write(data_to_write)
        print(f"Data written to {output_path}.")
except PermissionError:
    print(f"You do not have permission to write to {output_path}.")
except Exception as e:
    print(f"An error occurred: {e}")
    

append_path = "demo/append.txt"
data_to_append = "\nThis is a new line."
try:
    with open(append_path, "a") as file:
        file.write(data_to_append)
        print(f"Data appended to {append_path}.")
except PermissionError:
    print(f"You do not have permission to append to {append_path}.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
line_path = "demo/line.txt"

try:
    with open(file=line_path, mode="a") as file_a:
        file_a.writelines(
            ["\nLine 1", "\nWrite line2"]
        )
        file_a.close()
    
    with open(file=line_path, mode="r") as file:
        line = file.readline()
        print("Lines from the file:")
        for line in file:
            print(line.strip())
        file.close()
except FileNotFoundError:
    print(f"File {line_path} not found.")
except Exception as e:
    print(f"An error occurred: {e}")