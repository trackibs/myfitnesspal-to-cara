import myfitnesspal
import csv
import io

from datetime import date, timedelta, datetime

# Create a file name based on this year's data
thisFileName = "MFPData.csv"

f = open(thisFileName, "w")

#writer.write("Date,Tracking,String Value, Numerical Value, Additional Information")
f.write("Date,Tracking,String Value, Numerical Value, Additional Information\n")
f.close()

client = myfitnesspal.Client('my_fitness_pal_username')

d1 = date(2017, 10, 1)  # start date
d2 = date(2019, 1, 1)  # end date

delta = d2 - d1         # timedelta

for i in range(delta.days + 1):
    entrydate = d1 + timedelta(i)
    day = client.get_date(entrydate)
    print entrydate.strftime('%Y-%m-%d')
    for meal in day.meals:
        for entry in meal:
            f = open(thisFileName, "a")
            rowTimestamp = entrydate.strftime('%Y-%m-%d') + " " + datetime.strptime(str(meal).split(" ")[3], '%I:%M%p').strftime('%H:%M:%S')
            rowTracking = "Food"
            rowStringValue = "\"P" + str(entry.totals['protein']) + " C" + str(entry.totals['carbohydrates'])  + " F" + str(entry.totals['fat']) + "\""
            #rowStringValue = "P" + str(entry.totals['protein']) + " C" + str(entry.totals['carbohydrates'])  + " F" + str(entry.totals['fat'])
            rowNumericalValue = str(entry.totals['calories'])
            rowAdditionalInformation = "\"" + entry.short_name.encode('UTF-8') + "\""
            myrow = [rowTimestamp,rowTracking,rowStringValue,rowNumericalValue,rowAdditionalInformation]
            f.write(",".join(myrow) + "\n")
            print myrow
            f.close()

print(" -- Done.")
f.close()
