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


def detect_naming_convention(text: str) -> str:
    """
    Detect the naming convention of a given string.

    Returns:
        One of:
        - 'snake_case'
        - 'camelCase'
        - 'PascalCase'
        - 'kebab-case'
        - 'Title Case'
        - 'UPPER_CASE'
        - 'lowercase'
        - 'unknown'
    """
    if re.fullmatch(r'[a-z]+(_[a-z]+)+', text):
        return "snake_case"
    if re.fullmatch(r'[a-z]+([A-Z][a-z0-9]*)+', text):
        return "camelCase"
    if re.fullmatch(r'([A-Z][a-z0-9]*)+', text):
        return "PascalCase"
    if re.fullmatch(r'[a-z]+(-[a-z]+)+', text):
        return "kebab-case"
    if re.fullmatch(r'([A-Z][a-z]+)(\s[A-Z][a-z]+)*', text):
        return "Title Case"
    if re.fullmatch(r'[A-Z]+(_[A-Z]+)+', text):
        return "UPPER_CASE"
    if re.fullmatch(r'[a-z]+', text):
        return "lowercase"
    return "unknown"