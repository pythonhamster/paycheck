name = input("what is your name?: ")
regpay = float(input("what is your hourly pay?: "))
ovrpay = (regpay / 2) + regpay

hwork = float(input("how many hours did you work this week?: "))

if hwork >= 40:
    ovrhours = hwork - 40
    payck = (40 * regpay) + (ovrhours * ovrpay)
else:
    payck = hwork * regpay

print(f"{name.title()} earned ${payck:.2f} this week!")