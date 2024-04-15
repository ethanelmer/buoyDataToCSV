import csv




def file_parse(file):
    fileData = open(file)
    fileInfo = open(file)
    filelines = len(fileInfo.readlines())
    count = 0
    #data = dataLine.split()
    with open('BuoyData2023.csv', 'w', newline='') as csvfile:
        fieldnames = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Wave Height','Direction Dominant Period','Average Wave Period', 'Tide']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        while count < (filelines-1):
            if count == 0:
               csvinfo = fileData.readline()
               CSVSplit = csvinfo.split()
               # csvinfo = 18 separate tokens
               #print("CSV INFO: " + csvinfo)
               units = fileData.readline()
               UnitSplit = units.split()
               # units = 18 separate tokens
               #print("UNITS: " + units)
            else:
                #                           yr, mo, dy, hr, mn,WVHT,DPD,APDTIDE
                # numbers = 18 separate tokens   0 , 1,  2 , 3, 4, 8,9,10, 17
                numbers = fileData.readline()
                numSplit = numbers.split()
                #print("Line " + str(count) + ": " + numbers)
                dataLine = (CSVSplit[0]+" "+CSVSplit[1]+" "+CSVSplit[2]+" "+CSVSplit[3]+" "+CSVSplit[4]+" "+CSVSplit[8]+" "+CSVSplit[9]+" "+CSVSplit[10]+" "+CSVSplit[17]+
                            " "+UnitSplit[0]+" "+UnitSplit[1]+" "+UnitSplit[2]+" "+UnitSplit[3]+" "+UnitSplit[4]+" "+UnitSplit[8]+" "+UnitSplit[9]+" "+UnitSplit[10]+" "+UnitSplit[17]+
                            " "+numSplit[0]+" "+numSplit[1]+" "+numSplit[2]+" "+numSplit[3]+" "+numSplit[4]+" "+numSplit[8]+" "+numSplit[9]+" "+numSplit[10]+" "+numSplit[17])
                data = dataLine.split()
                numbers = data[18:27]
                writer.writerow(
                    {'Year': numbers[0], 'Month': numbers[1], 'Day': numbers[2], 'Hour': numbers[3], 'Minute': numbers[4],
                     'Wave Height': numbers[5], 'Direction Dominant Period': numbers[6],'Average Wave Period':numbers[7],'Tide':numbers[8]})
            count += 1

if __name__ == '__main__':
    file_parse(r'C:\Users\EElme\PycharmProjects\csvFileParsing\venv\BouyData2023.txt')


