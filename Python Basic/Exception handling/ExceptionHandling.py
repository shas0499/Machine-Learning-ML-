try:
    num = int(input("Enter a number : "))
    print(10/num)
except Exception as e:
    print(f"Exception Occured - {type(e).__name__} Exception")
else:
    print("Execution Success...")
finally:
    print("---- Thank You ------")