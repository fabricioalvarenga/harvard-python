import re

email: str = input("What's your email? ").strip()

regexp = r"^[a-zA-Z0-9.!#$%'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

if re.search(regexp, email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end of the string or just before the newline at the end of the string
# [] set of characters
# [^] complementing the set (i.e. [^@] has the effect of saying this is the set of characters that has everything except @ sign)
# \d decimal digit
# \D not a decimal digit
# \s whitespace character
# \S not a whitespace character
# \w word character ... as well as numbers and the underscore
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version
