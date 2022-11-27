sum = 0
def addToBankAccount(x):
    global sum
    sum += x

def substractFromBankAccount(x):
    global sum
    sum -= x


def moneyConversion(sum, a, b):
    match a, b:
        case "USD" as a, "KZT" as b:
            return sum * 470
        case "KZT" as a, "USD" as b:
            return sum / 470


addToBankAccount(500)
print(sum)

substractFromBankAccount(200)
print(sum)

print(moneyConversion(300, "USD", "KZT"))