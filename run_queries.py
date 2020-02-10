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