max_number = 3
current = max_number
while True:
    index = 2
    is_factor_of_all = True
    while index <= max_number:
        if current % index != 0:
            is_factor_of_all = False
            break
        index = index + 1
    if is_factor_of_all == True:
        print(f"{current} is the lcm")
        break
    current = current + max_number