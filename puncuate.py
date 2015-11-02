""" Capitalize the sentence and end with correct markup """


def dec(text):
    """ Create a declarative sentence """
    formatted = '%s%s.' % (text[0].capitalize(), text[1:len(text)])
    return formatted
