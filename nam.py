"""Taks 1"""


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# subject_marks.sort(key= lambda x : len(x[0]), reverse=True )
# """This function sorts the list primarily by the number of letters in the first element, 
# and secondarily in alphabetical order"""
# print(subject_marks)


"""Taks 2"""


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = filter(lambda x : not bool(x % 2), numbers)
# """This function checks if there are even numbers in the list"""
# print(list(result))


"""Task 3"""



# def protected(func):
#     """This decorator checks if a user is authorized to execute the decorated function"""
#     def wrapped():
        
#         username = input('Username: ')
#         password = input('Password: ')
        
#         check = lambda a, b : func() if a == 'admin' and b == 'admin' else print('You are not authorized')
        
#         return check(username, password)
    
#     return wrapped


# def public():
#     print("Hello World!")

# @protected
# def private():
#     print("Welcome, admin!")

# public()
# private()


"""Taks 4"""



def wrap_with(tag = 'strong'):
    """This function wraps other funtions with HTML tags"""
    def decorator(func):
    
        
        rewrite_in_lambda = lambda *a, **b :f'<{tag}>{func(*a,**b)}</{tag}>'
        
        
        return rewrite_in_lambda
    
    return decorator



@wrap_with(tag='strong')
def get_full_name(a, b):
    
    return a + ' ' + b


def get_html_greeting():
    
    return 'Hello, World!'

@wrap_with(tag='p')
@wrap_with(tag='em')
def get_custom_html_greeting(first, last):
    
    return f'Hello, {get_full_name(first, last)}!'




print(get_custom_html_greeting("James", "Brown"))