done = False
choices = ['plain', 'bold', 'italic', 'link', 'header', 'inline-code', 'line-break', 'new-line', 'ordered-list', 'unordered-list']
special_commands = ['!help', '!done']
text_combined = ""


def help_print():
    return print("Available formatters: plain bold header new-line italic link inline-code ordered-list unordered-list line-break \nSpecial commands: !help !done")


def check_input():
    if choice == "plain":
        text = input("Text:")
    elif choice == "bold":
        text = input("Text:")
        text = "**" + text + "**"
    elif choice == "italic":
        text = input("Text:")
        text = "*" + text + "*"
    elif choice == "link":
        text = input("Label:")
        url = input("URL:")
        text = "[" + text + "]" + "(" + url + ")"
    elif choice == "header":
        level = int(input("Level:"))
        text = input("Text:")
        text = ("#" * level) + " " + text + "\n"
    elif choice == "inline-code":
        text = input("Text:")
        text = "`" + text + "`"
    elif choice == "new-line":
        text = "\n"
    return text


def format_ordered_list(row_count):
    result = ''
    for i in range(int(row_count)):
        result += f"{i + 1}. {input(f'- Row #{i + 1}: ')}\n"
    return result


def format_unordered_list(row_count):
    result = ''
    for i in range(int(int(row_count))):
        result += f"* {input(f'- Row #{i + 1}: ')}\n"
    return result


while not done:
    count = 1
    choice = input("Choose a formatter:")
    if choice == "!help":
        help_print()
    elif choice == "!done":
        done = True
        file = open('output.md', 'w')
        file.writelines(text_combined)
        file.close()
        break
    elif choice not in choices:
        print("Unknown formatting type or command")
    elif choice == "ordered-list":
        number = int(input("- Number of rows: "))
        number1 = -1
        while number1 < 0:
            print("The number of rows should be greater than zero")
            number1 = int(input("- Number of rows: "))
        else:
            text_combined += format_ordered_list(number1)
            print(text_combined)
    elif choice == "unordered-list":
        number = -1
        while number < 0:
            print("The number of rows should be greater than zero")
            number = int(input("- Number of rows: "))
        else:
            text_combined += format_unordered_list(number)
            print(text_combined)
    else:
        text_combined += check_input()
        print(text_combined)
