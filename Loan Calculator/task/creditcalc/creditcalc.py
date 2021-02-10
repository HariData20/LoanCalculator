import argparse
import sys
from math import ceil, log

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)
# write your code here
print('Enter the loan principal:')
loan_principal = int(input())
print('''
What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
''')
option = input()
if option == 'm':
    print('Enter the monthly payment:')
    monthly_payment = int(input())
    no_of_months = ceil(loan_principal / monthly_payment)
    print('It will take', no_of_months, 'months' if no_of_months > 1 else 'month', 'to repay the loan')
elif option == 'p':
    print('Enter the number of months:')
    no_of_months = int(input())
    monthly_payment = loan_principal / no_of_months
    last_payment = 0
    if ceil(monthly_payment) != monthly_payment:
        last_payment = loan_principal - (no_of_months - 1) * ceil(monthly_payment)
        print('Your monthly payment =', ceil(monthly_payment), 'and the last payment =', last_payment, '.')
    else:
        print('Your monthly payment =', int(monthly_payment))

# Annuity payment
print('''
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
''')
choice = input()
if choice == 'n':
    print('Enter the loan principal:')
    loan_principal = int(input())  # P
    print('Enter the monthly payment:')
    monthly_annuity_payment = float(input())  # A
    print('Enter the loan interest:')
    interest = float(input()) / (12 * 100)
    no_of_months = ceil(log((monthly_annuity_payment /
                             (monthly_annuity_payment - interest * loan_principal)), 1 + interest))
    if no_of_months % 12 == 0:
        print(f'It will take {int(no_of_months / 12)}'
              , 'years' if no_of_months > 12 else 'year', 'to repay this loan!')
    elif no_of_months < 12:
        print(f'It will take {no_of_months}'
              , 'months' if no_of_months > 1 else 'month', 'to repay this loan!')
    elif no_of_months % 12 != 0:
        print(f'It will take {int(no_of_months // 12)} years and {int(no_of_months % 12)}'
              , 'months' if no_of_months % 12 > 1 else 'month'
              , 'to repay this loan!')

elif choice == 'a':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter the number of periods:')
    no_of_months = int(input())
    print('Enter the loan interest:')
    interest = float(input()) / (12 * 100)
    monthly_annuity_payment = loan_principal * (interest * pow(1 + interest, no_of_months)
                                                / ((pow(1 + interest, no_of_months)) - 1))
    print(f'Your monthly payment = {monthly_annuity_payment}!')


elif choice == 'p':
    print('Enter the annuity payment:')
    monthly_annuity_payment = float(input())
    print('Enter the number of periods:')
    no_of_months = int(input())
    print('Enter the loan interest:')
    interest = float(input()) / (12 * 100)
    loan_principal = monthly_annuity_payment / (interest * pow(1 + interest, no_of_months)
                                                / ((pow(1 + interest, no_of_months)) - 1))
    print(f'Your loan principal = {loan_principal}!')

# CLI Differentiated Payment

args = sys.argv
if len(args) == 5:
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--principal', type=int)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=int)
    args = parser.parse_args()
    if args.type not in ['diff', 'annuity']:
        print('Incorrect parameters')
        sys.exit()
    over_payment = 0
    if args.type == 'diff' and args.principal is not None and args.periods is not None and args.interest is not None \
            and args.payment is None:
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
            sys.exit()
        diff_payment = 0
        total_payment = 0
        interest = args.interest / (12 * 100)
        for i in range(args.periods + 1):
            i += 1
            diff_payment = ceil((args.principal / args.periods) + interest *
                                (args.principal - (args.principal * (i - 1) / args.periods)))
            print(f'Month {i} payment is {diff_payment}')
            total_payment += diff_payment
        over_payment = total_payment - args.principal
        print('Overpayment =', over_payment)

    elif args.type == 'annuity' and args.interest is not None and args.interest > 0:
        interest = args.interest / (12 * 100)
        if args.principal is None:
            if (args.payment is not None and args.payment > 0) and (args.periods is not None and args.periods > 0):

                loan_principal = ceil(args.payment / (interest * pow(1 + interest, args.periods)
                                                      / ((pow(1 + interest, args.periods)) - 1)))
                print(f'Your loan principal = {loan_principal}!')
                over_payment = (args.payment * args.periods) - loan_principal
                print('Overpayment =', over_payment)
            else:
                print('Incorrect parameters')
                sys.exit()
        elif args.periods is None:
            if (args.payment is not None and args.payment > 0) and (args.principal is not None and args.principal > 0):
                no_of_months = ceil(log((args.payment /
                                         (args.payment - interest * args.principal)), 1 + interest))
                if no_of_months % 12 == 0:
                    print(f'It will take {int(no_of_months / 12)}'
                          , 'years' if no_of_months > 12 else 'year', 'to repay this loan!')
                elif no_of_months < 12:
                    print(f'It will take {no_of_months}'
                          , 'months' if no_of_months > 1 else 'month', 'to repay this loan!')
                elif no_of_months % 12 != 0:
                    print(f'It will take {int(no_of_months // 12)} years and {int(no_of_months % 12)}'
                          , 'months' if no_of_months % 12 > 1 else 'month'
                          , 'to repay this loan!')
                over_payment = (args.payment * no_of_months) - args.principal
                print('Overpayment =', over_payment)
            else:
                print('Incorrect parameters')
                sys.exit()
        elif args.payment is None:
            if (args.principal is not None and args.principal > 0) and (args.periods is not None and args.periods > 0):
                monthly_annuity_payment = ceil(args.principal * (interest * pow(1 + interest, args.periods)
                                                                 / ((pow(1 + interest, args.periods)) - 1)))
                print(f'Your annuity payment = {monthly_annuity_payment}!')
                over_payment = (monthly_annuity_payment * args.periods) - args.principal
                print('Overpayment =', over_payment)
            else:
                print('Incorrect parameters')
                sys.exit()

    else:
        print('Incorrect parameters')
        sys.exit()
else:
    print('Incorrect Parameters')
    sys.exit()
