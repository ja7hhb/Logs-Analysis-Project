# -Logs Analysis-Project-

## -Introduction-

## This project is part of Full Stack Nanodegree.
Use the given database to analyze the data for the given three questions. ##

Question is:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The database includes three tables:

1. Authors table:
Includes information about the authors of articles.
2. Articles table:
Includes the articles themselves.
3. Log table:
Includes one entry for each time a user has accessed the site.

## -Installation-

1. Install [Python3](https://www.python.org/downloads/) and [Vagrant](https://www.vagrantup.com/downloads.html), [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Download or clone from [github fullstack-nandegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
3. Now we got newsdata.sql in our vagrant directory and now we are good to go.

## -How to run-

1. Change directory to vagrant directory then
type this command to run the vagrant on vm:
```
$ vagrant up
```

2. Then type this command to login into vm:
```
$ vagrant ssh
```

3. Change directory to /vagrant:
```
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$ 
```

4. Load the data to load database, using this command:
 ```
 vagrant@vagrant:/vagrant$ psql -d news -f newsdata.sql
 ```

5. Connect to the database:
```
vagrant@vagrant:/vagrant$ psql -d news
psql (9.5.11)
Type "help" for help.

news=> 
```

6. Create Views:
```
news=> create view title_view as select articles.title,
articles.author, COUNT(*) as view from log inner join 
articles on log.path like '%' || articles.slug 
where log.path!='/' and log.status='200 OK' GROUP BY 
articles.title, articles.author order by view desc;
```

7. Return to /vagrant directory and type `python3 log.py`, then output is like this:
```
vagrant@vagrant:/vagrant$ python3 log.py

What are the most popular three articles of all time?
Candidate is jerk, alleges rival -- 338647 views
Bears love berries, alleges bear -- 253801 views
Bad things gone, say good people -- 170098 views

Who are the most popular article authors of all time?
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views

On which days did more than 1% of requests lead to errors?
2016-07-17 -- 2.26 %errors
```
