address = "https://www.google.com/?q=regex"

parsed_address = address.split('/')
print parsed_address[2]

import re
m1 = re.search(r'', '  d ddd ddd ')
m2 = re.search(r'[^hello$]', 'what aobut hello selo/??! bla')
print m1, m2
