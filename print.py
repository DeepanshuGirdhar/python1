a=5      # datatype of variable is dynamically according to the value assign to it.only single line comment is possible in python.
spy_name=raw_input("enter name please")     # to scan input from user,
print a+5 # + used for concatination without any delimeter(space) ,(comma) used for concatinate with delimeter. "" and '' both used for string
spy_name="Welcome"+" "+spy_name+" "+"in python world"
print spy_name
check=int(raw_input("enter any no")) #raw _input function returns string value.
# python is dynamically typed assigned datatype language.

if check==1:
    print "p no."
elif check>1:
    for i in range(2,check):
        if check%i==0:
            print "not p no."
            break;
        else:
             print "p no."
             break;

