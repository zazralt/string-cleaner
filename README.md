# String Cleaner
String Cleaner is a Python library for cleaning and normalizing text.

## Installation
```bash
pip install git+https://github.com/zazralt/string-cleaner.git
```

## Usage
```python
from string_cleaner import *

detect_naming_convention("foo_bar")

df['name'] = df['name'].apply(lambda name: remove_multiple_whitespaces(name))

```
