def get_percentage(num, dec=None):
    if dec is None:
        num = round(num * 100)
    else:
        num = round((num * 100), dec)
    return "{}%".format(num)
