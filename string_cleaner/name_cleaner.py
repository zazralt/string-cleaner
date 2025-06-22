import re
import unicodedata

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

def capitalize_after_space(text):
    return re.sub(r'(?<=\s)([a-z])', lambda m: m.group(1).upper(), text)

def remove_outer_whitespace(text):
    return text.strip()

def remove_multiple_whitespaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def remove_non_ascii(text):
    return ''.join(char for char in text if ord(char) < 128)

def remove_non_alphabetic(text):
    return re.sub(r"[^A-Za-z\s-]", '', text)

def remove_non_alphanumeric(text):
    return re.sub(r"[^A-Za-z0-9\s-]", '', text)

def replace_ampersand(text):
    return text.replace('&', 'and')

def replace_dashes_with_hyphen(text):
    for dash in ['–', '—', '−']:
        text = text.replace(dash, '-')
    return text

def replace_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

def lowercase_minor_words(text):
    minor_words = [
        "A", "And", "As", "At", "But", "By", "Down", "For", "From", "If",
        "In", "Into", "Like", "Near", "Nor", "Of", "Off", "On", "Once",
        "Onto", "Or", "Over", "Past", "So", "Than", "That", "To", "Upon",
        "When", "With", "Yet"
    ]

    # Replace each word with its lowercase equivalent when surrounded by whitespace
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
