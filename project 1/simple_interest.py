# collect p,t,r
# calculate the monthly payment and show to the user 

def main():
    print("SIMPLE INTREST CALCULATOR")
    print("")

    p = float(input("Enter the loan amount: "))
    apr = float(input("Enter the anual interest rate: "))
    time = int(input("Enter the amount of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = time * 12
    monthly_payment = p * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print("The monthly payment for this loan is: %.2f " % monthly_payment) 

main()

