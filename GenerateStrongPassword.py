import string
import array
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
allList = s1+s2+s3+s4

def passGen():
    length = int(input("Enter the length of password \n"))
    temp_pass = random.choice(s1) + random.choice(s2) + random.choice(s3) + random.choice(s4)
    for i in range(length-4):
        temp_pass = temp_pass + random.choice(allList)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    password= ""
    for x in temp_pass_list:
        password+=x
    return password

def validatePassword(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in s4 for char in password):
        score += 1
    
    # evaluate the password strength
    if score <= 2:
        return "Weak "
    elif score == 3:
        return "moderate"
    elif score == 4:
        return "good"
    elif score >= 5:
        return "Strong"
    else:
        return "Invalid"
    
        
    