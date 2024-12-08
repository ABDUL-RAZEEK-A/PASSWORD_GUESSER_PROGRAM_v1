import datetime,random,string

'''
----------------------------------------------------------------------------------------------------
THIS IS A BASIC PASSWORD GUESSER WHERE YOU CAN ENTER THE DETAILS AND YOU CAN GET WHAT YOU WANT
THIS IS ONLY FOR EDUCATIONAL PURPOSE

FUNCTIONS:

    $ print_pass([combinations])
   . $ common_pass()
   . $ gen_random_pass([length],[size])
   . $ generate_passwords(<name>,<DOB>)
    $ write_file(<passwords>,[file_name],[file_extention]):
   . $ guess_password(<name>,[DOB],[sub_details])

I AM HERE BY DONE THIS PROJECT WITH MY KNOWLEDGE AND I DIDNOT USE IT FOR MALPRACRICE CLAIM
----------------------------------------------------------------------------------------------------
'''
def write_file(passwords,file_name='passwords',ext='.txt'):
    with open(file_name+ext, 'w') as file:
        for item in passwords:
            file.write(str(item) + '\n')
    return "open on "+file_name+ext
        

def print_pass(passwords):

    '''This helps to print the password in the table form as n X 5
    And too it returns the total password count for each occurences
    '''
    
    print("\nThese are the resulted passwords you can try : \n")
    c=0
    values=[]
    for val in passwords:
        print(val)
        values.append(val)
        c+=1
        if(c==300):
            choice=input("\npassword generator more than 300.Sholud i stop the program(y or n)").lower()
            #it may slow down your program and takes more memory.Do it on our own risk
            #<slow while printing the password only>
            if choice == 'y' or choice == 'yes':
                break;
            
            
    values=list(set(values))
    print("Total count :",c)
  
def common_pass():
    
    '''
    ------------------------------------------------------------------------------------------------
    These are the common passwords used randimly in the world ,and you may think of it while creating a password,
    So what you are looking for also can be mentioned here....
    ------------------------------------------------------------------------------------------------'''
    
    return ['123456', 'password', '123456789', '12345', '12345678','qwerty', 'abc123', '111111', '123123', 'admin',
               'letmein', 'welcome', 'monkey', '1234', 'password1','sunshine', '123qwe', '123', '1q2w3e4r', 'qwerty123',
               '123321', '1qaz2wsx', 'qwertyuiop', 'iloveyou', 'trustno1','password123', 'dragon', '1qazxsw2', 'baseball', 'superman',
               '123abc', 'password1!', 'shadow', 'qazwsx', 'welcome1','sunshine1', '1234abcd', '12345abc', 'football', '1password',
               '112233', 'asdfgh', '123123123', 'qazwsxedc', '1234qwer','654321', '123abc456', 'password!@#', '123qweasd', '987654321',
               'hackerx','244466666','007',]


def gen_random_pass(length=8,size=20):
    l=[]
    for _ in range(size):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        l.append(password)
    return l



def generate_passwords(name,dob,):
    possible_passwords = []
    possible_passwords.append('iam' + name)
    possible_passwords.append(name + '007')
    possible_passwords.append(name.lower())
    possible_passwords.append(name.lower() + dob)
    possible_passwords.append(dob)
    possible_passwords.append(name.lower() + "123")
    possible_passwords.append(name.lower() + "!")
    possible_passwords.append(name.lower() + dob[-2:])
    possible_passwords.append(name.capitalize() + dob)
    possible_passwords.append(dob + name.lower())
    for i in "!@#$%^&*()_-+=<>?/.,';:\" ":
        possible_passwords.append(name+i+dob[:4])
        possible_passwords.append(name + ''.join(i for i in dob[2:] if i not in '0-'))
    return possible_passwords



def guess_password(name, dob='', extra_info=[]):
    '''This is a simple password guesser function where you need to pass the arguments as
    <variable> = guess_pass(<NAME>, <DOB>,<EXTRA-INFO>)
    where both the arguments are strings and the DOB is in 'DDMMYYYY' format.
    The extra information is to given in list of strings to works on it to get the possibl results.....
    '''
    
    possible_passwords = []
    possible_passwords.append('iam' + name)
    possible_passwords.append(name + '007')
    possible_passwords.append(name.lower())
    possible_passwords.append(name.lower() + dob)
    possible_passwords.append(dob)
    possible_passwords.append(name.lower() + "123")
    possible_passwords.append(name.lower() + "!")
    possible_passwords.append(name.lower() + dob[-2:])
    possible_passwords.append(name.capitalize() + dob)
    possible_passwords.append(dob + name.lower())
    for i in "!@#$%^&*()_-+=<>?/.,';:\" ":
        possible_passwords.append(name[:3]+i+dob[:4])
        possible_passwords.append(name+i+dob)
        possible_passwords.append(name+i+dob[::2])
        
    for extra in extra_info:
        possible_passwords.append(name.lower() + extra)
        possible_passwords.append(extra + name.lower())
        possible_passwords.append(name.lower() + extra.capitalize())
        possible_passwords.append(extra.capitalize() + name.lower())
        possible_passwords.append(name.lower() + dob + extra)
        possible_passwords.append(extra + dob + name.lower())
        possible_passwords.append(extra + "123")
        possible_passwords.append(extra + "!" + name.lower())
        possible_passwords.append(name.lower() + extra + "2022")
        for i in "!@#$%^&*()_-+=<>?/.,';:\" ":
            for j in "!@#$%^&*()_-+=<>?/.,';:\" ":
                possible_passwords.append(name+i+dob+j+extra)
                possible_passwords.append(name[:3]+i+dob[:4]+j+extra)
                possible_passwords.append(name[:3]+i+dob[:4]+j+extra[:3])
                possible_passwords.append(name+i+dob[::2]+j+extra)

                
    for i in range(int(dob[-4:]),datetime.datetime.now().year):
        possible_passwords.append(name.lower()+str(i))
        for j in "!@#$%^&*()_-+=<>?/.,';:\" ":
            possible_passwords.append(name.lower()+str(j)+str(i))
            
    possible_passwords.append(name.lower() + "!" + dob[-2:])
    possible_passwords.append(name.capitalize() + "!" + dob[-2:])

    return possible_passwords
