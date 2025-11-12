# create a simple calculator that can evaluate 
# math expressions and recall previous calculations
class Calculator:
    def __init__(self):
        self._memory = [] # to store previous calculations

    # evaluate the math expression
    def calculate(self, query):
        return eval(query)
    
    # store the result and print it
    def canvas(self, text):
        result = {text: self.calculate(text)} # store as dict in the list
    
        self._memory.append(result)
        print(f"Result: {self.calculate(query)}")

    # recall previous calculations
    def recall(self):
        x = input(f"How many last calculations to recall among {len(self._memory)} calculations?")
        try:
            n = int(x)
            return self._memory[-n:]
        except:
            return "Invalid input for recall."
            
casio = Calculator() # create an instance of Calculator

while True:
    query = input("Enter a math expression (or 'exit to to quit, 'recall' to see history):")
    
    if query.lower() == 'exit':
        print("Exiting calculator.")
        print("Calculation History:")
        for i in casio._memory:
            key_name = list(i.keys())[0] # get the expression from the dict keys and then print
            print(f"Result: {key_name} = {i[key_name]}")
        break

    elif query.lower() == 'recall':
        for record in casio.recall():
            key_name = list(record.keys())[0] # get the expression from the dict keys and then print
            print(f"Result: {key_name} = {record[key_name]}")
    
    else:
        casio.canvas(query)
