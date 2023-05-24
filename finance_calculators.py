import math
# The program allows user to access two financial calculators;
# An investment calculator and the other one is loan  repayment calculator
print("Investment-To calculate the amount of interest you'll earn on your investment.")
print("Bond-To calculate the amount you'll have to pay on a home loan.")

# The user choose which calculator they want to use 
choice=input("Enter either 'investment' or 'bond' from the menu above to proceed : ").lower()

# if the user enter neither of the choices an error message will pop upin
if choice!="investment" and choice!="bond":
    print("Invalid option!\n Please Enter 'investment' or 'bond'")
    choice=input("Enter 'investment'or 'bond' to proceed : ").lower()
    
#if the user select investment,  will calculate the total investment
if choice== "investment" :
    
         capital=float(input("Enter the amount you want to deposit : "))
         rate=float(input("Enter the interest rate : "))
         r=rate/100
         time=float(input("Period of investment : "))
         interest=str(input("Choose'simple' and 'compound' interest : ").lower())     
        
         # if the user enter neither of the choices,
         # an error message will pop up
         if interest!='simple' and interest!="compound":
             print("Invalid option!\nChoose only'simple' or 'compound'!")
             interest=str(input("Enter 'simple'or compound' : ").lower())
            
         #calculating either simple or compound interest 
         if interest=="simple" :
             simple_interest=capital*(1+(r*time))
             print(f"The total is R{simple_interest}")
         else :
             if interest=="compound":
                 compound_interest=capital*math.pow((1+r),time)
                 print(f"The total is R{compound_interest}")
                 

elif choice=="bond" :
    p=float(input("Please enter the present value of the house : "))
    interest=float(input("Enter the interest rate : "))
    i=((interest/100)/12)
    n=float(input("Enter the time interval the bond will be repaid : "))
    repayment=round((i*p)/(1-(1+i)**(-n)),2)
    print(f"Repayment=R{repayment}")
    
    
    
                                 ########### end #################
