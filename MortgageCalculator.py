import locale
locale.setlocale(locale.LC_ALL, "")
# constants
number_of_months = 12
percent = 100

#input variables
principal = int(input("Principal: "))
annual_interest_rate = float(input("Annual Interest Rate: "))
period = int(input("Period (year): "))

#mortgage calculation
monthly_interest = annual_interest_rate/percent/number_of_months
number_of_payments = period * number_of_months

mortgage = principal * ((monthly_interest*((1+monthly_interest)**number_of_payments))/((1+monthly_interest)**(number_of_payments-1)))

# format mortgage to currency and print value 
mortgage_formatted = locale.currency(mortgage)
print("Mortgage: " + mortgage_formatted) 

