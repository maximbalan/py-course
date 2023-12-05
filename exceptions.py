# import pendulum

# # try:
# #     num = int(input("Enter a number: "))
# #     r = 10 / num
# #     print("Result: ", r)
# # except ZeroDivisionError:
# #     print("Cannot divide by zero")
# # except ValueError:
# #     print("Invalid input")
# # except Exception as e:
# #     print("Error: ", e)
# # else:
# #     print("No error")
# # finally:
# #     print("Finally")

# now = pendulum.now()

# def calculate_age(birth_year):
#     current_year = now.year
#     if birth_year > current_year:
#         raise ValueError("Birth year cannot be greater than current year")
#     return current_year - birth_year

# try:
#     birth_year = int(input("Enter your birth year: "))
#     age = calculate_age(birth_year)
#     print("Your age is:", age)
# except ValueError as e:
#     print("Error:", e)

class InsufficientFundsException(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsException("Insufficient funds in the account")
    return balance - amount

try:
    account_balance = 1000
    withdrawal_amount = int(input("Enter the withdrawal amount: "))
    remaining_balance = withdraw(account_balance, withdrawal_amount)
    print("Remaining balance:", remaining_balance)
except InsufficientFundsException as e:
    print("Error:", e)
    