def capitalize(words):
    uppercase = ""
    for n in words:
        uppercase += n.capitalize() + " "
    return uppercase[0:-1]