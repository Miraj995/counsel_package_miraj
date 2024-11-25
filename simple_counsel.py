import json


# Function to read and print JSON file
def print_json_file(file_path):
    try:
        # Open the JSON file for reading
        with open(file_path, 'r') as file:
            # Load the JSON data
            data = json.load(file)

            # Print the JSON data
            print(json.dumps(data, indent=4))  # Pretty print with indentation
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")


# Specify the path to your JSON file
json_file_path = '/home/miraj-raha/Downloads/results.json'

# Call the function to print the JSON file
print_json_file(json_file_path)