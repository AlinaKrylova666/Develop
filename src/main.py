from src.utils import load_transactions

file_path = '../data/transactions.json'
transactions = load_transactions(file_path)

print(transactions)


from decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

if __name__ == "__main__":
    print(my_function(1, 2))
