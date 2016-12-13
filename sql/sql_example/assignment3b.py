import sqlite3

choice = ''

while choice.lower() != 'exit':
    prompt = """Select an aggregation or to exit. Your options are:
    'MAX'
    'MIN'
    'SUM'
    'AVG'
    'EXIT'
    Your choice:  """
    choice = raw_input(prompt)
    if choice.lower() == 'exit':
        break

    with sqlite3.connect('newnum.db') as conn:
        c = conn.cursor()
        c.execute("SELECT {}(num) FROM numbers;".format(choice))
        output = c.fetchall()[0][0]
        print "The {} of the data is {} \n\n".format(choice, output)
