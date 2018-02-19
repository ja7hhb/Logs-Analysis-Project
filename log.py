#!/usr/bin/env python3
import psycopg2
try:
    conn = psycopg2.connect(database="news")
except:
    print("Coudn't connect to the database")

query1 = "select * from title_view limit 3;"
query2 = "select authors.name, sum(view) from title_view, authors \
where title_view.author=authors.id \
group by authors.name order by sum(view) desc;"
query3 = "with day_view_count as (select time::timestamp::date as date1, \
count(*) as view_count from log group by date1), \
day_error_count as (select time::timestamp::date as date2, \
count(*) as error_count from log where status != '200 OK' group by date2) \
select date1, view_count, error_count from day_view_count, day_error_count \
where date1 = date2 and error_count > 0.01 * view_count \
group by view_count, error_count, date1;"

cur = conn.cursor()
cur.execute(query1)
print("\nWhat are the most popular three articles of all time?")
for row in cur.fetchall():
    print(row[0], "--", row[2], "views")

cur = conn.cursor()
cur.execute(query2)
print("\nWho are the most popular article authors of all time?")
for row in cur.fetchall():
    print(row[0], "--", row[1], "views")

cur = conn.cursor()
cur.execute(query3)
print("\nOn which days did more than 1% of requests lead to errors?")
for row in cur.fetchall():
    print(row[0], "--", round((row[2]/row[1]*100), 2), "%errors")

conn.close()
