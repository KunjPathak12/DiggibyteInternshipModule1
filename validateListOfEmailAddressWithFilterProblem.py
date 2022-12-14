import re
def fun(s):
    if re.search("^[\w-]+@[a-zA-Z0-9]+\.[a-zA-z]{1,3}$",s):
        return True
    else:
        return False
    # return True if s is a valid email, else return False

