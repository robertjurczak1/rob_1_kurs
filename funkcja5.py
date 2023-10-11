# def compute_use_total(amount_in_aud=0, amount_in_gbp=0):
#     total = 0
#     total += amount_in_aud * 0.78
#     total += amount_in_gbp * 1.29
#     return total

def compute_use_total(amount_in_aud=0, amount_in_gbp=0):
    total = 0
    total += convert_currency(amount_in_aud, 0.78)
    total += convert_currency(amount_in_gbp, 1.29)
    return total

def convert_currency(amount, rate, margin=0)
    return amount * rate (1+margin)

print(compute_use_total(amount_in_gbp=10))
