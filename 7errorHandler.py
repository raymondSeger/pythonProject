def this_fails():
    x = 1/0

#in python, they use except instead of catch
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
finally:
    print('Goodbye, world!')

#custom exception, needs 1 parameter
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

#raise to throw an error
try:
    raise CustomException('HiThere')
except CustomException as err:
    print('An exception flew by!')
    print(err.message)
