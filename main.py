history = []

def main():
    operation = input("Enter a mathematical operation ('h' for operation history): ")
    if operation.lower() == "h":
        for ops in history:
            print(ops)
            main()

    try:
        result = eval(operation)
        print(f"The result is: {result}")
        history.append(f"{operation} = {result}")
    except Exception as e:
        print(f"No mathemetical operation found! ({e})")
    main()

if __name__ == "__main__":
    main()