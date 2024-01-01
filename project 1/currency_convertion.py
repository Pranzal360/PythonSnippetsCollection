def main():
    print("this program converts us dollars to pounds ")
    print("")

    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print(f"{dollars} dollars = {pounds} pounds")

convert_to_pounds = lambda dollars: dollars * 0.82

main()