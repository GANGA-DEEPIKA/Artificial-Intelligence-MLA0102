START

data ← list of (outlook, humidity, actualOutput)

correct ← 0

FOR each (outlook, humidity, actualOutput) in data DO

    IF outlook = "Overcast" THEN
        predicted ← "Yes"

    ELSE IF outlook = "Sunny" THEN
        IF humidity = "High" THEN
            predicted ← "No"
        ELSE
            predicted ← "Yes"
        END IF

    ELSE IF outlook = "Rain" THEN
        predicted ← "Yes"
    END IF

    IF predicted = actualOutput THEN
        correct ← correct + 1
    END IF

END FOR

accuracy ← correct / total number of records
PRINT accuracy

END
