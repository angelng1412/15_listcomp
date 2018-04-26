def check(password):
    uppers = [ c for c in password if c.isupper() ]
    lowers = [ c for c in password if c.islower() ]
    nums = [ c for c in password if c.isdigit() ]
    if (len(uppers) == 0 or len(lowers) == 0 or len(nums) == 0):
	return False
    else:
        return True
        
print check('22ndo2jkjA') #true
print check('32heo8r3UWije2in') #true
print check('klkdhfosjdf23j') #false
print check('KDF2JD92J29') #false 
print check('23348918') #false
print check('passWord') #false


def strength(password):
    uppers = [ c for c in password if c.isupper() ]
    lowers = [ c for c in password if c.islower() ]
    nums = [ c for c in password if c.isdigit() ]
    chars = [ c for c in password if not(c.isalnum()) ]
    sum = 2*len(uppers) + len(lowers) + 2*len(nums) + 3*len(chars)
    sum = sum / 2
    if sum > 10:
        return 10
    return sum

print strength('qwerty');
print strength('qweRTY');
print strength('qweRTY123');
print strength('qweRTY123!@#');
print strength('pa');
print strength('pass');
print strength('paSS');
print strength('paSS123'); 
