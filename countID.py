from threading import Thread
import glob
import sqlite3


def get_total_cost(name_file):
    row_record = {}
    open_file = open(name_file, 'r')
    row_one = 0
    for line in open_file.readlines():
        if row_one == 0:
            row_one = 1
            continue
        string = [i[1:-2] for i in line.split(',')]
        customer_id = string[-1]
        cost = float(string[-3])
        if len(customer_id) < 40:
            continue
        if customer_id not in row_record:
            row_record[customer_id] = cost
        else:
            row_record[customer_id] += cost
    sorted_row = sorted([(value, key) for (key, value) in row_record.items()],
                                                                reverse=True)
    write_to_database(sorted_row, 'mysql')


def write_to_database(text, name):
    connect = sqlite3.connect('bd/%s.sqlite' % name)
    c = connect.cursor()
    try:
            c.execute('''create table stocks (cost text, id text)''')
    except:
        pass
    for t in text:
        c.execute('''insert into stocks values (?,?)''', t)
    connect.commit()
    c.execute('select * from stocks order by id ')
    c.close()
location_of_the_file = glob.glob("C:/Users/SergiyBudz/PycharmProjects/countID/cvs-file/*.csv")

if __name__ == '__main__':
    for x in location_of_the_file:
        print('File_name:\t' + str(x) + '\n')
        Thread(target=get_total_cost(x)).start()
