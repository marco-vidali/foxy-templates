import os


def replace_placeholders(template, values):
    folder_path = "./templates/"
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    template_file = files[template - 1]

    file_content = ""
    with open(os.path.join(folder_path, template_file), 'r') as file:
        file_content = file.read()

    for placeholder, value in values.items():
        file_content = file_content.replace(f'{{{{{placeholder}}}}}', value)

    output_dir = "./output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, f"{template_file}")
    with open(output_file_path, 'w') as output_file:
        output_file.write(file_content)

    return output_file_path
