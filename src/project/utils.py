def keys(thing):
    "Returns a string containing all of a 'thing's keys for debugging purposes."
    return '\n'.join([key for key in dir(thing) if '__' not in key])
