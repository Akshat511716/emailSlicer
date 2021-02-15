email = input("Enter your email address: ")
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
format = print(f"Username is {username} and domain is {domain} ")