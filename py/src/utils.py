def print_colored(text, color_code):
    """
    Prints the given text in the specified ANSI color.

    Args:
    text (str): The text to print.
    color_code (str): The ANSI color code to use.
    """
    return f"\033[{color_code}m{text}\033[0m"

# Usage examples:
# print_colored("This is an informational message.", "92")  # Green
# print_colored("This is a warning message.", "93")        # Yellow
# print_colored("This is an error message.", "91")         # Red