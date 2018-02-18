Logs Analysis-Project

Introduction

This project includes a Vagrant virtual environment and VirtualBox. To use it, install VirtualBox and (Vagrant), and follow the project installation steps bellow.

Installation

1.Install Vagrant and VirtualBox
2.Download or clone from github fullstack-nandegree-vm repository
3.Now we got newsdata.sql in our vagrant directory and now we are good to go.

How to run

change directory to vagrant directory then
type this command to run the vagrant on vm
$ vagrant up

then type this command to login into vm
$ vagrant ssh

Change directory to /vagrant, so lools like this
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$ 

Load the data to load database, using this command:
 psql -d news -f newsdata.sql

Creating Views
news=> create view title_view as select articles.title, articles.author, COUNT(*) as view from log inner join articles on log.path like '%' || articles.slug where log.path!='/' and log.status='200 OK' GROUP BY articles.title, articles.author order by view desc;

output:

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
