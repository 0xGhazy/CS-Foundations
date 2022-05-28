if __name__ == '__main__':
    
    # flag_vars
    is_alphanumeric = False 
    is_alphabetical = False
    is_digits = False
    is_lowercase = False
    is_uppercase = False
    s = input()

    for i in s:
        if i.isalnum():
            is_alphanumeric = True
            break
    
    for i in s:
        if i.isalpha():
            is_alphabetical = True
            break

    for i in s:
        if i.isdigit():
            is_digits = True
            break
    
    for i in s:
        if i.islower():
            is_lowercase = True
            break
    for i in s:
        if i.isupper():
            is_uppercase = True
            break

    print(is_alphanumeric)
    print(is_alphabetical)
    print(is_digits)
    print(is_lowercase)
    print(is_uppercase)
