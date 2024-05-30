#functions with outputs
def format_name(f_name, l_name):
    #doctstring
    """take first and last name and format it to return title case version of the name"""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
print(format_name("angela", "ANGELA"))

