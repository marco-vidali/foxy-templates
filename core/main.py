from functions import output, input, file


def main():
    output.clear()
    output.banner()
    output.templates()
    template = input.template()
    print()
    values = input.placeholder_values(template)
    file.replace_placeholders(template, values)
    print()
    output.success("Custom template created in the \"output\" folder")
