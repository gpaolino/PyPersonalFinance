# my_utilities
import datetime


# Coverter for decimal separator
def decimal_separator_substitution(val, default_val=None):
    try:
        return val.replace(',','.')
    except ValueError:
        return default_val

# Coverter for string "dd/MM/yyyy" to date
def string_to_date(val, default_val=None):
    try:
        return datetime.datetime.strptime(val,"%d/%m/%Y")
    except ValueError:
        return default_val
