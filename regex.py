#regex

import re
pattern=re.compile(r'[0-9-+]')

str="109-_"
print(bool(pattern.search(str)))
