import data 

def form_res(res:bool, massage:str):
    if res:
        return f'{massage}'
    else:
        return 'Something went wrong'

def show_books(): 
    '''The function processes data about all books.'''
    return '\n'.join([f"{k} -- {v[0]} -- {v[2]} -- {v[1]} -- {v[3][0]} -- {v[3][1]}" for k,v in data.show_books()])

def found(index:int): 
    '''Returns set with the requested data.'''
    work_var = data.show_books_val()
    return set(work_var[str(k)][index] for k in work_var)

def show_book_by_name(name:str): 
    '''The function provides data about the requested book.'''
    return '\n'.join([f"{k} -- {v[0]} -- {v[1]} -- {v[3][0]} -- {v[3][1]}" for k,v in data.show_books() if v[2]==name])

def show_author(name:str): 
    '''The function provides data about all books of a particular author.'''
    return '\n'.join([f"{k} -- {v[2]} -- {v[1]} -- {v[3][0]} -- {v[3][1]}" for k,v in data.show_books() if v[0]==name])
        
def show_series(name:str):  
    '''The function provides data about all books of a particular series.'''
    return '\n'.join([f"{k} -- {v[0]} -- {v[2]} -- {v[3][0]} -- {v[3][1]}" for k,v in data.show_books() if v[1] == name])

def add_books(article:int, quantity:int):
    '''The function adds the books selected by the article to the cart.\n
    article - article of the book in the data.\n
    quantity - the number of books ordered.'''
    if data.control_art(article) is False:
        return '\nA book with such an article is not in the database.'
    elif data.control_count(article,quantity) is False:
        return '\nThere are not enough copies of the selected book in stock.'
    else:    
        res = data.add_books(article,quantity)
        return form_res(res,'\nThe book has been successfully added to the cart.')
    
def show_cart(): 
    '''The function shows all books in the cart.'''
    if data.show_cart() == '-1':
        return "The cart is empty."
    else:
        work_var = data.show_cart()
        return '\n'.join([f"{k} - -- - {v[1]} -- {v[2]} -- {v[3][0]} -- {v[3][1]}" for k,v in work_var])

def remove_books(num: int): 
    '''The function removes one selected book from the order.\n
    num - the number of the book in the cart'''
    if data.control_remove(num):
        res = data.remove_books(num)
        return form_res(res, '\nThe book was successfully deleted from the order.')
    else:
        return '\nThere is no book with this number in the сart.'

def cleaning():
    '''The function clears the cart.'''
    res = data.cleanind_and_return()
    return form_res(res,'\nThe cart is cleared.')

def list_for_registration(): 
    '''The function displays a list of orders for processing.'''
    work_var = data.place_order()
    return '\n'.join([f"{v[1]} - {v[2]}, count: {v[3][1]} " for v in work_var])

def calc_price(): 
    '''The function calculates the total amount of the order.'''
    price = 0
    work_var = data.place_order()
    for i in work_var:
        price += i[3][0] * i[3][1]
    return price

def place_order():
    '''The function places an order.'''
    inform = f'{list_for_registration()},\nprice: {calc_price()}.'
    data.cleaning()
    return inform

def redact_order(num:int,count:int):
    '''The function changes the number of books in the selected order line number.\n
    num - num - the number of the book in the cart.\n
    count - the number of books ordered.'''
    if data.control_remove(num) is False:
        return '\nThere is no book with this number in the сart.'
    elif data.control_count_cart(num,count) is False:
        return '\nThere are not enough copies of the selected book in stock.'
    else:
        res = data.redact_order(num,count)
        return form_res(res,'\nThe number of books in the order has been successfully changed.')
