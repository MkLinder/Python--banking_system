def name_formatter(name):
    formatted_name = ''
    name = name.split(' ')
    
    for word in name:
        formatted_name += f"{word.capitalize()} "

    return formatted_name    