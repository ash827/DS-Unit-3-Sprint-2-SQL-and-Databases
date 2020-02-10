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