import re

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
        - ''
    """
    if re.fullmatch(r'[a-z0-9]+(_[a-z0-9]+)+', text):
        return "snake_case"
    if re.fullmatch(r'[a-z0-9]+([A-Z][a-z0-9]*)+', text):
        return "camelCase"
    if re.fullmatch(r'([A-Z][a-z0-9]+)+', text):
        return "PascalCase"
    if re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)+', text):
        return "kebab-case"
    if text.title() == text:
        return "Title Case"
    if re.fullmatch(r'[A-Z0-9]+(_[A-Z0-9]+)+', text) or re.fullmatch(r'[A-Z0-9]+', text):
        return "UPPER_CASE"
    if re.fullmatch(r'[a-z0-9]+', text):
        return "lowercase"
    return ""

def check_name(name: str) -> str:
    result = ""
    if contains_acronym(name):
      result += 'contains acronym'
    return result

def contains_acronym(name: str) -> bool:
    """
    Checks if the given name contains an acronym.
    An acronym is defined as:
      - Two or more consecutive uppercase letters (e.g., NASA, BMW)
      - Possibly surrounded by parentheses or followed by a period

    Args:
        name (str): The input name to check.

    Returns:
        bool: True if an acronym is found, False otherwise.
    """
    pattern = re.compile(r'\b(?:[A-Z]{2,}|\([A-Z]{2,}\)|[A-Z](?:\.[A-Z])+)\b')
    return bool(pattern.search(name))
