


def temp_conversion():
    try:
        user_input = float(input("Please enter the temperature in Farenheit: "))
        celsius_temp = (user_input - 32) * 5/9
        print(f"The temperature in Celsius is {celsius_temp:.2f}°")  
    except (TypeError, ValueError):
        print("Please enter a numerical value.")
    
    else:
        print(f"{int(user_input)}° Farenheit converts to {celsius_temp:.2f}° Celsius.")
    finally:
        print("Thanks for using the weather forecast application!")

temp_conversion()