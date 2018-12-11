import xlrd
import csv
import pandas


def csv_from_excel():
    wb = xlrd.open_workbook('excel.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('base.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    wr.writerow(["Spam"] * 5)

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()


def read():
    with open('base.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))



def dictread():
    with open('base.csv') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            print(row["Element "])


def panda():

    df = pandas.read_csv('base.csv')

    print(df["Mass of AMU"])

