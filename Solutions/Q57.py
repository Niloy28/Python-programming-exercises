# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

import re

email_id = input()

pattern = r"([\w._]+)@([\w._]+)[.](com)"
match = re.search(pattern, email_id)

if match:
    print(match.group(1))
