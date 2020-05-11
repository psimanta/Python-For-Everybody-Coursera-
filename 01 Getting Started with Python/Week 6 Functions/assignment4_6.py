def computepay(h,r):
    if h > 40:
        h = 40 + (h-40)*1.5
    return h*r

hrs = input("Enter Hours:")
rate = input("Rate: ")
hrs = float(hrs)
rate = float(rate)
p = computepay(hrs,rate)
print("Pay",p)
