
# ^ use to define start with
# $ use to define end with
regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'

import re

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())