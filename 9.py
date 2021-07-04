def computepay(h,r):
    if h > 40:
        p = 40 * r + (h - 40) * r * 1.5
    if h < 40:
        p = + h * r
    return p


hours = input("how many hours: ")
rph = input("rate per hour: ")
fh = float(hours)
fr = float(rph)

print('Pay',computepay(fh, fr))