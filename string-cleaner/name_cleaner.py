import re

def camel_to_snake(name: str) -> str:
    """
    Convert CamelCase or camelCase to snake_case.

    Args:
        name (str): The input string in CamelCase or camelCase.

    Returns:
        str: The converted string in snake_case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()