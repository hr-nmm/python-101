with open("portfolio.csv") as file:
    # portfolio = [row.rstrip().split(",") for row in file][1:]
    # portfolio = [[holding[0],int(holding[1]),float(holding[2])] for holding in portfolio]
    try: 
        portfolio = [[holding[0],int(holding[1]),float(holding[2])] for holding in [row.rstrip().split(",") for row in file][1:]]
    except ValueError or IndexError as err: ## "as err" stores the error message in 'err' varible
        print(f'Reason: {err}')
    else: print(portfolio)

## Note: When an exception is handled, program execution resumes with the statement that immediately follows the last except block. The program does not return to the location where the exception occurred.


## 'raise' keyword is used to intentionally raise exceptions within your code. You need to give the name of an exception.
raise RuntimeError("Computer Says No")  