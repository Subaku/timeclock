
def register(*decorators):
    '''
    ' Nifty snippet that takes an args of decorators for a method
    ' and call them appropriately while setting a _decorators property 
    ' on the original method.  The property contains a tuple of the 
    ' decorator methods.
    '''

    def registerWrapper(func):
        for dec in decorators[::-1]:
            func = dec(func)

        func._decorators = decorators
        return func

    return registerWrapper


def login_exempt(func):
    '''
    ' Custom decorator that marks the function with the property 
    ' _decorators so that it can be recognized later.
    '''

    func._decorators = (login_exempt,)
    return func
