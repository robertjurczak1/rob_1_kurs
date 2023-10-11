def pass_reff(list1=[]):
    list1.extend([22, 33])
    print("lista wewnątrz funkcji", list1)

def ff(cyfra):
    global a
    a = 10 # tutaj a jest zdefiniowane wewnętrznie
    cyfra = a +4
    print("a wewnątrz", cyfra)

a=0 # tutaj a jest zdefiniowane zewnętrznie

ff(a)
print(a)
list1 = [12, 76, 90]
pass_reff(list1)
print(list1)