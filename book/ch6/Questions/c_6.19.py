class Empty(Exception):
    """ Error attempting to access an element from an empty container. """
    pass
class ArrayStack:
    """ LIFO Stack  implementation using a Python list as underlying storage. """
    
    def __init__ (self):
        """ Create an empty stack. """
        self._data = []

    def len (self):
        """ Return the number of elements in the stack. """
        return len(self._data)

    def is_empty(self):
        """ Return True if the stack is empty."""
        return len(self._data) == 0
    
    def push(self, e):
        """ Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """
            Return (but do not remove) the element at the top of the stack.
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty(): raise Empty('Stack is empty')
        
        return self._data[-1]
        
    def pop(self):
        """ 
            Remove and return the element from the top of the stack (i.e., LIFO).
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


"""
    Illustraing the use case of the stack ADT for
    validating if an html code is valid or not.
"""
def is_matched_html(raw):
    """ Return True if all HTML tags are properly matched; False otherwise. """
    S = ArrayStack()
    j = raw.find('<')

    while j != -1:
        k = raw.find('>', j + 1)

        if k == -1: return False

        tag = raw[j + 1: k]

        if not tag.startswith('/'):
            S.push(tag.split()[0])
        else:
            # If it was not a closing tag and they were not any opening tags
            if S.is_empty(): return False
            # If the opening and closing tags are not the same thing
            if tag[1:] != S.pop(): return False
        
        j = raw.find('<', k + 1)

    return S.is_empty()

raw_html = """
    <body>
        <center attribute1="value1" attribute2="value2">
            <h1> The Little Boat </h1>
        </center>
        <p>     
            The storm tossed the little boat like a cheap 
            sneaker in an old washing machine. The three 
            drunken fishermen were used to such treatment, 
            of course, but not the tree salesman, who even 
            as a stowaway now felt that he had overpaid for 
            the voyage. 
        </p>
        <ol>
            <li> Will the salesman die? </li>
            <li> What color is the boat? </li>
            <li> And what about Naomi? </li>
        </ol>
    </body>
"""

print(is_matched_html(raw_html))