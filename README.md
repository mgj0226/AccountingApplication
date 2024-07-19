# AccountingApplication
This is an application for accounting.

1. (DONE) Setup the Django project and React App.

2. Setup the database in models.py.
    2.1 Table Transaction:
        . Username (FK)
        . Account
        . date
        . Amount of expense / income / Transfer
        . Category
        . Shop
        . Description
    2.2 Table User:
        . Username (PK)
        . Accounts' balance
    2.3 Table Account:
        . Username (FK)
        . AccountName
        . AccountType
        . Balance
