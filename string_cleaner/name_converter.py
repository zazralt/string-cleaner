# camelToSnake > camel_to_snake
def camel_to_snake(name):
    return ''.join(['_'+char.lower() if char.isupper() else char for char in name])

# snake_to_camel > snakeToCamel
def snake_to_camel(name):
    name = name.split('_')
    return name[0].lower() + ''.join(word.title() for word in name[1:])

# PascalToSnake > camel_to_snake
def pascal_to_snake(name):
    return ''.join(['_'+char.lower() if char.isupper() else char for char in name])[1:]

# snake_to_pascal > SnakeToPascal
def snake_to_pascal(name):
    return ''.join(word.title() for word in name.split('_'))

# Title To Snake > title_to_snake
def title_to_snake(name):
    return '_'.join(word.lower() for word in name.split(' '))

# Title To Camel > titleToCamel
def title_to_camel(name):
    name = name.split(' ')
    return name[0].lower() + ''.join(word.title() for word in name[1:])

# Title To Pascal > TitleToPascal
def title_to_pascal(name):
    return ''.join(word.title() for word in name.split(' '))
