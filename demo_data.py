import sqlite3

#establishing a connection to sqlite3
def connection(demo_data):
	conn = sqlite3.connect(demo_data)
	return conn

#creating the table with columns s,x,y...
#using create_script is just like using ''' in Slack! 
#Something I found using GOOGLEFOO

def create_table(c, conn):
	create_script = '''
	CREATE TABLE demo(
	s TEXT NOT NULL,
	x INT NOT NULL,
	y INT NOT NULL
	);
	'''
	c.execute(create_script)
	conn.commit()
	return

#Inserting the data of each column
def insert_data(c,conn):
	c.execute('INSERT INTO demo VALUES("g",3,9);')
	c.execute('INSERT INTO demo VALUES("v",5,7);')
	c.execute('INSERT INTO demo VALUES("f",8,7);')
	conn.commit()
	return

#Checking to see if it works
def output_check(cur):
    for row in cur.execute(
        'SELECT * FROM demo'):
        print(row[1])
    return

#defining our queries we'd like to run
def run_queries(cur):
    #1.How many rows
    qry = 'SELECT COUNT(*) FROM demo ORDER BY demo.x;'
    for row in cur.execute(qry):
        print('demo table has ', row[0], ' rows')

    # 1. How many rows in Demo where x and y are at least 5
    qry = '''
    SELECT COUNT(*)
    FROM demo
    WHERE demo.x >= 5 AND demo.y >= 5
    ORDER BY demo.x;
    '''
    for row in cur.execute(qry):
        print('There are ', row[0], ' rows where both x and y are at least 5')

    # 2. How many distinct values
    qry = 'SELECT COUNT(DISTINCT demo.y) FROM demo GROUP BY demo.y;'
    ctr = 0
    for row in cur.execute(qry):
        ctr = ctr+1
    print('demo table has', ctr, 'distint values of y')
    qry = 'SELECT COUNT(DISTINCT demo.x) FROM demo GROUP BY demo.x;'
    ctr = 0
    for row in cur.execute(qry):
        ctr = ctr+1
    print('demo table has', ctr, 'distint values of x')
    qry = 'SELECT COUNT(DISTINCT demo.s) FROM demo GROUP BY demo.s;'
    ctr = 0
    for row in cur.execute(qry):
        ctr = ctr+1
    print('demo table has', ctr, 'distint values of s')

    return

#defining our main connection
def main():
    conn = connection('demo_data.sqlite3')
    cur = conn.cursor()

    run_queries(cur)

    cur.close()
    conn.close()
    return

#Launch from command line 
if __name__ == '__main__':
    main()


#Example of code run in GitBash:
#$ python demo_data.py
#demo table has  3  rows
#There are  2  rows where both x and y are at least 5
#demo table has 2 distint values of y
#demo table has 3 distint values of x
#demo table has 3 distint values of s