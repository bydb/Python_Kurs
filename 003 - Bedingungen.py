
# hier wird das Alter abgefragt und geschaut ob man minderjährig ist!
alter = int(input("Wie alt bist du?: "))
if alter > 18:
    print("Du bist volljährig.")
else:
    print("Du bist minderjährig.")


# hier wird eine Zahl abgefragt und geschaut ob sie in definierten Zahlenbereichen ist!
number = int(input("Gebe ein Zahl ein: "))

if number < 0:
    print("Die Zahl ist negativ.")
elif number <= 10:
    print("Die Zahl ist zwischen 0 und 10 (inclusive).")
elif number <= 20:
    print("Die Zahl ist zwischen 0 und 20 (inclusive).")
else:
    print("DIe Zahl ist größer als  20.")
