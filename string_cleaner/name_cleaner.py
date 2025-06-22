import re
import unicodedata

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
    
def capitalize_after_space(text: str) -> str:
    """
    Capitalizes the first lowercase letter that follows any whitespace character.

    Args:
        text (str): The input string.

    Returns:
        str: String with letters capitalized after whitespace.
    """
    return re.sub(r'(?<=\s)([a-z])', lambda m: m.group(1).upper(), text)

def remove_outer_whitespace(text: str) -> str:
    """
    Removes leading and trailing whitespace from the input string.

    Args:
        text (str): The input string.

    Returns:
        str: Trimmed string with no leading or trailing whitespace.
    """
    return text.strip()

def remove_whitespaces(text: str) -> str:
    """
    Removes all whitespace characters from the string.

    Args:
        text (str): The input string.

    Returns:
        str: String with all whitespace removed.
    """
    return re.sub(r'\s+', '', text).strip()

def remove_multiple_whitespaces(text: str) -> str:
    """
    Replaces multiple consecutive whitespace characters with a single space.

    Args:
        text (str): The input string.

    Returns:
        str: Cleaned string with normalized spacing.
    """
    return re.sub(r'\s+', ' ', text).strip()

def remove_non_ascii(text: str) -> str:
    """
    Removes all non-ASCII characters from the input string.

    Args:
        text (str): The input string.

    Returns:
        str: ASCII-only string.
    """
    return ''.join(char for char in text if ord(char) < 128)

def remove_non_alphabetic(text: str) -> str:
    """
    Removes all characters except alphabetic letters, spaces, and hyphens.

    Args:
        text (str): The input string.

    Returns:
        str: String with only letters, spaces, and hyphens.
    """
    return re.sub(r"[^A-Za-z\s-]", '', text)

def remove_non_alphanumeric(text: str) -> str:
    """
    Removes all characters except letters, digits, spaces, and hyphens.

    Args:
        text (str): The input string.

    Returns:
        str: Cleaned alphanumeric string.
    """
    return re.sub(r"[^A-Za-z0-9\s-]", '', text)

def remove_non_utf8(text: str) -> str:
    """
    Removes invalid UTF-8 characters by encoding and decoding the string.

    Args:
        text (str): The input string.

    Returns:
        str: UTF-8 compliant string.
    """
    return text.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')

def remove_round_brackets(text: str) -> str:
    """
    Removes content enclosed in round brackets including the brackets.

    Args:
        text (str): The input string.

    Returns:
        str: String without round bracketed content.
    """
    return re.sub(r"[\(].*?[\)]", '', text)

def remove_square_brackets(text: str) -> str:
    """
    Removes content enclosed in square brackets including the brackets.

    Args:
        text (str): The input string.

    Returns:
        str: String without square bracketed content.
    """
    return re.sub(r"[\[].*?[\]]", '', text)

def remove_curly_brackets(text: str) -> str:
    """
    Removes content enclosed in curly brackets including the brackets.

    Args:
        text (str): The input string.

    Returns:
        str: String without curly bracketed content.
    """
    return re.sub(r"[\{].*?[\}]", '', text)

def remove_angle_brackets(text: str) -> str:
    """
    Removes content enclosed in angle brackets including the brackets.

    Args:
        text (str): The input string.

    Returns:
        str: String without angle bracketed content.
    """
    return re.sub(r"[\<].*?[\>]", '', text)
    
def remove_windows_special_characters(text: str) -> str:
    """
    Removes common Windows special/control characters, such as non-breaking spaces,
    carriage returns, soft hyphens, and other non-printable or control characters.

    Args:
        text (str): The input string.

    Returns:
        str: Cleaned string without Windows-specific control characters.
    """
    # Replace specific Windows characters explicitly
    replacements = {
        '\u00A0': ' ',  # Non-breaking space
        '\u200B': '',   # Zero-width space
        '\u200E': '',   # Left-to-right mark
        '\u200F': '',   # Right-to-left mark
        '\u202A': '',   # LRE
        '\u202B': '',   # RLE
        '\u202C': '',   # PDF
        '\u202D': '',   # LRO
        '\u202E': '',   # RLO
        '\uFEFF': '',   # BOM
        '\u00AD': '',   # Soft hyphen
        '\r': '',       # Carriage return (may be redundant if using `strip()` already)
    }

    for char, replacement in replacements.items():
        text = text.replace(char, replacement)

    # Optionally remove all control characters (ASCII 0–31, except \n and \t if needed)
    text = ''.join(ch for ch in text if ch == '\n' or ch == '\t' or ord(ch) >= 32)

    return text
    
def replace_ampersand(text: str) -> str:
    """
    Replaces all ampersands ('&') with the word 'and'.

    Args:
        text (str): The input string.

    Returns:
        str: String with '&' replaced by 'and'.
    """
    return text.replace('&', 'and')

def replace_dashes_with_hyphen(text: str) -> str:
    """
    Replaces en dash (–), em dash (—), and minus sign (−) with a standard hyphen (-).

    Args:
        text (str): The input string.

    Returns:
        str: String with all types of dashes replaced by hyphens.
    """
    for dash in ['–', '—', '−']:
        text = text.replace(dash, '-')
    return text

def replace_accents(text: str) -> str:
    """
    Removes accents from characters by decomposing Unicode characters.

    Args:
        text (str): The input string.

    Returns:
        str: ASCII-equivalent string without accents.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

def lowercase_minor_words(text: str) -> str:
    """
    Converts minor English words (e.g., 'and', 'in', 'with') to lowercase if surrounded by whitespace.

    Args:
        text (str): The input string.

    Returns:
        str: String with minor words lowercased (not affecting start/end or punctuation-adjacent).
    """
    minor_words = [
        "A", "And", "As", "At", "But", "By", "Down", "For", "From", "If",
        "In", "Into", "Like", "Near", "Nor", "Of", "Off", "On", "Once",
        "Onto", "Or", "Over", "Past", "So", "Than", "That", "To", "Upon",
        "When", "With", "Yet"
    ]

    for word in minor_words:
        pattern = r'(?<=\s){}(?=\s)'.format(re.escape(word))
        text = re.sub(pattern, word.lower(), text)

    return text

def normalize_notation(name: str, notation: str = 'default', case: str = 'default', delimiter: str = ' ', preserve_case: bool = False) -> str:
    """
    Convert a string into a specified notation format.

    Parameters:
        name (str): Input string to format.
        notation (str): 'default', 'snake', 'camel', 'pascal', or 'title'.
        case (str): 'default', 'lower', 'upper', 'title', 'capitalize'.
        delimiter (str): Delimiter to use (e.g., ' ', '_', '').
        preserve_case (bool): If True, do not modify letter case.

    Returns:
        str: The formatted string.
    """

    # clean notation
    name = re.sub('([a-z0-9])([A-Z])', r'\1 \2', name)          # space for camel cases
    name = re.sub('([A-Z])([A-Z])([a-z]+)', r'\1 \2\3', name)   # space after acronyms
    name = re.sub('([0-9])([a-z])', r'\1 \2', name)             # space after numbers
    name = re.sub('([A-z])([0-9])', r'\1 \2', name)             # space before numbers
    name = ' '.join(word for word in name.split('_'))           # clean snake cases
    name = re.sub('[^A-z0-9]', ' ', name).strip()               # replace special characters with delimiter
    name = re.sub('\s+', ' ', name).strip()                     # remove multiple spaces

    # prepare notation
    if notation == 'snake':
        case = 'lower'
        delimiter = '_'
    elif notation in ['pascal', 'camel']:
        case = 'title'
        delimiter = ''
    elif notation == 'title':
        case = 'title'
        delimiter = ' '

    # prepare case
    if not preserve_case:
        if case == 'default':
            if name.isupper():
                name = name.lower()
            else:
                # convert title to lower and leave acronyms upper
                name = ' '.join([word.lower() if word.istitle() else word for word in name.split()])
        if case == 'lower':
            name = name.lower()
        if case == 'upper':
            name = name.upper()
        if case == 'title':
            name = name.title()
        if case == 'capitalize':
            name = name.capitalize()

    # prepare delimiter
    if delimiter != ' ':
        name = re.sub(' ', delimiter, name)
    if notation == 'camel':
         name = name[:1].lower() + name[1:]

    return name
