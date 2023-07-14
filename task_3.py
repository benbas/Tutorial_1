## IF STATEMENTS

balance = 5000
txAmount = 400

if balance >= txAmount:
    # complete transaction
    balance -= txAmount
    print("Transaction of " + str(txAmount) + " completed.")
    print("Balance: " + str(balance))
elif balance < txAmount:
    # block transaction
    print("You do not have sufficient balance to transact")

## FOR LOOPS

cities = ['Brisbane', 'Sydney', 'Beijing']

for w in cities:
    print(w, len(w))

for i in range(5):
    print(i)


# To discuss: break and continue statements
# More information about compound statements, find here: https://docs.python.org/3/reference/compound_stmts.html
