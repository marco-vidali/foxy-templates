from termcolor import cprint
import os
from functions import output
import re


def fancy(text):
    cprint(f"[?] {text}:", "white", "on_black", end="")
    return input(" ")


def template():
    template = None

    try:
        template = int(fancy("Template"))
    except ValueError:
        output.error("Template not valid.")

    folder_path = "./templates/"
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    if template < 1 or template > len(files):
        output.error(f"Template {template} is not valid.")

    return template


def placeholder_values(template):
    folder_path = "./templates/"
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    template_file = files[template - 1]

    file_content = ""
    with open(os.path.join(folder_path, template_file), 'r') as file:
        file_content = file.read()

    placeholders = re.findall(r'{{(.*?)}}', file_content)

    values = {}
    processed_placeholders = set()

    for placeholder in placeholders:
        if placeholder not in processed_placeholders:
            user_input = fancy(f'{placeholder.capitalize()}')
            while not user_input.strip():
                output.error(f"{placeholder.capitalize()} cannot be empty.")
                user_input = fancy(f'{placeholder.capitalize()}')
            values[placeholder] = user_input
            processed_placeholders.add(placeholder)

    return values
