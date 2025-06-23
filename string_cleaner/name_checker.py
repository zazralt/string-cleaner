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

def check_name(name: str, separator: str = " ", ignore: str = "") -> str:
    """
    Evaluates a name string against multiple formatting and character rules.
    Skips non-alphabetic and non-alphanumeric checks for specified separator character.

    Args:
        name (str): The input name.
        separators (str): Characters to ignore in alphabetic and alphanumeric checks.

    Returns:
        str: A formatted string beginning with 'contains ...' listing issues,
             or an empty string if no issues are detected.
    """
    result = []

    if contains_outer_whitespace(name):
        result.append("outer whitespace")
    if contains_multiple_whitespaces(name):
        result.append("multiple whitespaces")
    if ignore != '':
        name = re.sub("["+ignore+"]", '', name)
    if contains_number(name):
        result.append("number")
    if contains_acronym(name):
        result.append("acronym")
    if contains_non_ascii(name):
        result.append("non-ASCII")
    if contains_unicode_dashes(name):
        result.append("unicode dashes")
    if contains_ampersand(name):
        result.append("ampersand")
    if contains_punctuation(name):
        result.append("punctuation")

    cleaned_name = re.sub(separator, '', name)
    cleaned_name = re.sub(r'[\d!"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]', '', cleaned_name)
    if any(not c.isalpha() for c in cleaned_name):
        result.append("non-alphabetic")
    if any(not c.isalnum() for c in cleaned_name):
        result.append("non-alphanumeric")

    return ', '.join(result) if result else ""


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

def contains_punctuation(s: str) -> bool:
    """
    Checks if the input string contains any ASCII punctuation characters using regex.
    
    Parameters:
        s (str): The input string to check.
    
    Returns:
        bool: True if any ASCII punctuation character is found, False otherwise.
    """
    return bool(re.search(r'[!"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]', s))
    
def contains_brackets(s: str) -> bool:
    """
    Checks if the input string contains any brackets: (), [], {}, <>.

    Args:
        s (str): The input string.

    Returns:
        bool: True if any bracket is found, False otherwise.
    """
    return bool(re.search(r'[\[\]\(\)\{\}\<\>]', s))

def contains_unicode_dashes(s: str) -> bool:
    """
    Checks if the input string contains any Unicode dash characters,
    including en dash, em dash, and minus sign.

    Args:
        s (str): The input string.

    Returns:
        bool: True if any Unicode dash character is found, False otherwise.
    """
    return any(c in s for c in ['–', '—', '−'])

def contains_ampersand(s: str) -> bool:
    """
    Checks if the input string contains an ampersand character '&'.

    Args:
        s (str): The input string.

    Returns:
        bool: True if '&' is present, False otherwise.
    """
    return '&' in s

def contains_number(s: str) -> bool:
    """
    Checks if the input string contains any numeric digits (0–9).

    Args:
        s (str): The input string.

    Returns:
        bool: True if at least one digit is found, False otherwise.
    """
    return any(char.isdigit() for char in s)
    
# contains_non_utf8
# contains_accents
