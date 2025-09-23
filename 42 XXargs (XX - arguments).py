# xxargs = xx arguments

def student(**details):
    print(details)
    print("CPI = ", details["CPI"])

student(id=101, name="Manik", CPI = 7.21)



"""

{'id': 101, 'name': 'Manik', 'CPI': 7.21}
CPI =  7.21

"""
