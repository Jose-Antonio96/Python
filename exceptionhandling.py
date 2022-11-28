try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))

    result = numerator / denominator

except ZeroDivisionError:
    print("You can't divide by zero! Baaaka!")
#except Exception:
#   print("something went wrong :(")
except ValueError:  
    print("Enter only numbers please")
else:
    print(result)
finally:
    print("This will always execute")

