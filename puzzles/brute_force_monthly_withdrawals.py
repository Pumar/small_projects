def runOutOfMonthsOrMoneyFirst(withdrawAmount, moneyLeft, monthsLeft):
    if monthsLeft <= 0:
        return "months", moneyLeft
    if moneyLeft <= 0:
        return "money", monthsLeft
 
    return runOutOfMonthsOrMoneyFirst(withdrawAmount, moneyLeft * 1.072 - withdrawAmount, monthsLeft - 1)
 
result = "UNKNOWN"
 
for withdrawAmount in xrange(1, 200000):
    outOfWhat, leftOver = runOutOfMonthsOrMoneyFirst(withdrawAmount, 200000, 120)
    print "Out of", outOfWhat, "Leftover:", leftOver
    if outOfWhat == "money":
        result = withdrawAmount
        break
 
print "Withdraw amount:", result