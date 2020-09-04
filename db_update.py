import psycopg2
conn = psycopg2.connect("host=gravtyqa10x.combkc64kri4.us-west-2.rds.amazonaws.com dbname=gravtyqa2 user=bol password=39itPSAXPTsiJ64fhgCriBdm")
cur = conn.cursor()
cur.execute('select * from cmrtest.members_member LIMIT 10')
one = cur.fetchone()
all = cur.fetchall()
print(all)

