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
    """
    Evaluates a name string against multiple formatting and character rules.

    Args:
        name (str): The input name.

    Returns:
        str: A semicolon-separated string describing the issues found.
             Returns an empty string if no issues are detected.
    """
    result = []

    if contains_acronym(name):
        result.append("contains acronym")
    if contains_multiple_whitespaces(name):
        result.append("contains multiple whitespaces")
    if contains_outer_whitespace(name):
        result.append("contains outer whitespace")
    if contains_non_ascii(name):
        result.append("contains non-ASCII characters")
    if contains_non_alphabetic(name):
        result.append("contains non-alphabetic characters")
    if contains_non_alphanumeric(name):
        result.append("contains non-alphanumeric characters")
    if contains_brackets(name):
        result.append("contains brackets")

    return "; ".join(result)

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

def contains_multiple_whitespaces(name: str) -> bool:
    """
    Checks if the input string contains multiple consecutive whitespace characters.

    Args:
        name (str): The input string (e.g., a full name).

    Returns:
        bool: True if multiple consecutive whitespaces are found, False otherwise.
    """
    return bool(re.search(r'\s{2,}', name))

def contains_outer_whitespace(name: str) -> bool:
    """
    Checks if the input string has leading or trailing whitespace.

    Args:
        name (str): The input string.

    Returns:
        bool: True if there is leading or trailing whitespace, False otherwise.
    """
    return name != name.strip()

def contains_non_ascii(s: str) -> bool:
    """
    Checks if the input string contains any non-ASCII characters.

    Args:
        s (str): The input string.

    Returns:
        bool: True if there are non-ASCII characters, False otherwise.
    """
    return any(ord(char) > 127 for char in s)

def contains_non_alphabetic(s: str) -> bool:
    """
    Checks if the input string contains any non-alphabetic characters.

    Args:
        s (str): The input string.

    Returns:
        bool: True if there are non-alphabetic characters, False otherwise.
    """
    return any(not char.isalpha() for char in s)

def contains_non_alphanumeric(s: str) -> bool:
    """
    Checks if the input string contains any non-alphanumeric characters.

    Args:
        s (str): The input string.

    Returns:
        bool: True if there are non-alphanumeric characters, False otherwise.
    """
    return any(not char.isalnum() for char in s)

def contains_non_utf8(b: bytes) -> bool:
    """
    Checks if the byte sequence is not valid UTF-8.

    Args:
        b (bytes): Input byte string.

    Returns:
        bool: True if the byte sequence is not valid UTF-8, False otherwise.
    """
    try:
        b.decode('utf-8')
        return False
    except UnicodeDecodeError:
        return True

def contains_brackets(s: str) -> bool:
    """
    Checks if the input string contains any brackets: (), [], {}, <>.

    Args:
        s (str): The input string.

    Returns:
        bool: True if any bracket is found, False otherwise.
    """
    return bool(re.search(r'[\[\]\(\)\{\}\<\>]', s))
