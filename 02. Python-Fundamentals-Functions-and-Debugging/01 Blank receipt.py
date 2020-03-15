#   Print a blank receipt via a function that calls 3 other functions
def print_header():
    print('CASH RECEIPT')
    print('-' * 30)

def print_body():
    print('Charged to' + '_' * (30 - len('Charged to')))
    print('Received by' + '_' * (30 - len('Received by')))

def print_footer():
    print('-' * 30)
    print('\u00A9 SoftUni')

def print_full_receipt():
    print_header()
    print_body()
    print_footer()

print_full_receipt()
