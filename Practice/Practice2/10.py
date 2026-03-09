# Total vehicles V and total wheels W are given.
# Find number of two-wheelers (T) and four-wheelers (F).
# Formula: T + F = V  and  2T + 4F = W  →  F = (W - 2V)/2, T = V - F
# Print 'INVALID INPUT' if F or T is negative or not whole number.

v = int(input("Enter Total Vehicles:"))
w = int(input("Enter Total Wheels:"))
if (w-2*v)%2 != 0:
    print("Invalid input")
else:
    f = (w - 2*v) // 2
    t = v - f
    if t < 0 or f < 0: 
        print('INVALID INPUT')
    else: 
        print('Two Wheelers:', t); print('Four Wheelers:', f)
