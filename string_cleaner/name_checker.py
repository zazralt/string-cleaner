import re

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
