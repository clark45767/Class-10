class Employee:
    # Initializing Constructor)
    def __init__(self):
        print('Employee created.')
    #Deleting (Destroctor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
obj= Employee()
del obj