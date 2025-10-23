import datetime

def denaryToBinary(integer):
    if integer == 0:
        return("0")
    else:
        out = ""
        while integer > 0:
            remainder = str(integer % 2)
            out = remainder + out
            integer = integer // 2
        return(out)

def addLeadingZeros(string, finalStringLength):
    tempString = "0" * finalStringLength + string
    finalString = tempString[-finalStringLength:]
    return(finalString)

def getBinaryTime():
    now = datetime.datetime.now()
    hourCount = addLeadingZeros(str(now.hour), 2)
    minuteCount = addLeadingZeros(str(now.minute), 2)
    secondCount = addLeadingZeros(str(now.second), 2)

    binaryHours = (addLeadingZeros(denaryToBinary(int(hourCount[0])), 2), addLeadingZeros(denaryToBinary(int(hourCount[1])), 4))
    binaryMinutes = (addLeadingZeros(denaryToBinary(int(minuteCount[0])), 3), addLeadingZeros(denaryToBinary(int(minuteCount[1])), 4))
    binarySeconds = (addLeadingZeros(denaryToBinary(int(secondCount[0])), 3), addLeadingZeros(denaryToBinary(int(secondCount[1])), 4))

    return(binaryHours, binaryMinutes, binarySeconds)
