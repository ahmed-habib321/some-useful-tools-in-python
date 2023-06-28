def update_file_with_new_strings(file_path, new_strings):
    """
    Updates a text file with new strings, removing duplicates.

    Args:
        file_path (str): The path to the text file.
        new_strings (list): A list of strings to be added.

    Returns:
        None
    """

    # Read the existing content from the file
    with open(file_path, 'r') as file:
        content = file.readlines()
        content = [line.strip() for line in content]

    # Add new strings (without duplicates) to the content
    for new_string in new_strings:
        if new_string not in content:
            content.append(new_string)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write('\n'.join(content))


# Usage example
file_path = 'path of text file.txt'
new_strings = ['text1', 'text2', 'text3', 'text4']
update_file_with_new_strings(file_path, new_strings)