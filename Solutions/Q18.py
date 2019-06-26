import re

s = input()
passwords = s.split(',')

accepted_passwords = []
for password in passwords:
    if len(password) >= 6 and len(password) <= 12:
        if not re.search("[a-z]", password):
            continue
        if not re.search("[A-Z]", password):
            continue
        if not re.search("[0-9]", password):
            continue
        if not re.search("[$#@]", password):
            continue

        accepted_passwords.append(password)

print(','.join(accepted_passwords))
