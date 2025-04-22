def main():

    fahrenheit = float (input("\033[1;3m Enter the temperature in fahrenheit:\033[0m"))

    celsius = (fahrenheit - 32.00) * (5.00/9.00)

    print(f"temperature : {fahrenheit}F = {celsius}C")
    
    
if __name__ == "__main__":
    main()
