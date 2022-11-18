# ************** WORKING WITH CSV FILE ******************
# CSV = comma separated value
#       simplified spread sheet as a plain text file.

import csv

# file = open("data.csv", "w")
# file.close()

# BETTER APPROACH TO WRITE AND READ
# with open("data.csv", "w") as file:
#     # writer(fileObj) method , with this we can write tabular data to our csv file
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])
# result = -- created a data.csv file with row data

# READ
with open("data.csv") as file:
    reader = csv.reader(file)
    # when we convert the reader to a list, we already at the end of the file
    print(list(reader))
    # print([row for row in reader])
    # result = [['transaction_id', 'product_id', 'price'], [], ['1000', '1', '5'], [], ['1001', '2', '15'], []]

    # this loop will not run because we cannot iterate twice
    for index, row in enumerate(reader):
        print(index, row)
