#If applicant has high income AND good credit
    #Eligible for loan
# AND: both
# OR: atleast one
# NOT: if applicant has good credit AND doesn't have a criminal record

#has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")