import csv

# with open('PythonNiUI\hest.csv', 'r') as csv:
#     data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-4]
#     # writer = csv.writer(file)
output = "jazz"
output1 = "90"

appender = [
    [output, output1]
            ]
file = open('PythonNiUI\hest.csv', 'a', newline='')
writer = csv.writer(file)
writer.writerows(appender)
file.close()

print(appender)