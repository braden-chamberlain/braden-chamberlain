# #     # import classes :
# # from pandas import DataFrame
# # from sklearn.linear_model import LinearRegression
# # from sklearn.ensemble import RandomForestClassifier
# #     # import functions :
# # from sklearn.metrics import mean_absolute_error

# ###actual imports :###
# import pandas as pd

# # build my class of type DataFrame
# # df hols a dataframe 'object'
# # when i create a new object and save it to a variable
# # i say that I have 'instantiated' that object
# # object oriented programming ^^^
# df = pd.DataFrame({'a':[1,2,3], 'b': [4,5,6]})

# if __name__ == '__main__':
# # variables that form part of an 'object'
# # are called 'attributes'
# # we will access them using 'dot-notation'
#     # print(df.shape) 
#     # print(df.dtypes)
#     # print(df.columns)

# # funtions that form part of an 'object'
# # are called 'methods'
    
#     # print(df.head())
#     # print(df.describe())
#     # print(df.isnull().sum())

class Wallet:
    #first thing to run when we make a new class
    # outline required user-provided input values here
    # parameters with default parameters assigned are optional
    def __init__(self, initial_amount = 0):
        #save the user-provided initial_amount as an attribute
        #self refers to whatever object I'm working with
        self.balance = initial_amount

    #spend cash "METHOD"
    def spend_cash(self, amount):
        if self.balance < amount:
            return 'Not enough money'
        else:
            self.balance = self.balance - amount
            return f"remaining balance: ${self.balance}"
        
    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f'New balance of: ${self.balance}'


    #__repr__ method
    #changes hgow the 'object' looks when it is printed out
    # the presense of the self keywork allows me to access
    # or modify class attributes within this function
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"

if __name__ == '__main__':
    wallet1 = Wallet(500)
    print(wallet1.spend_cash(240))
    print(wallet1.spend_cash(90))
    print(wallet1.add_cash(160))
    wallet2 = Wallet(50)
    wallet3 = Wallet(3000)
