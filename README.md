# TournamentResults
##
### Overview

This is the 4th project in Udacity Full Stack Web Developer Nanodegree. The Objective for this project is to write Python module that uses PostgreSQL database to keep track of players and matches in a game tournament.

This project also introduces the concept of utilizing the power of virtual machine and unit test for software devleopment.

### Setup
1. Install [Vagrant](http://vagrantup.com/) and [VitrualBox](https://www.virtualbox.org/).
2. Clone the [fullstack-nanodegree-vm repository](http://github.com/udacity/fullstack-nanodegree-vm) to get the Vagrant setup file.
3. Clone [this repository](https://github.com/jtang10/TournamentResults) to your local machine and replace all the files in `vagrant/tournament/`
4. Launch Vagrant VM.
5. To perform the unit test, type `python tournament_test.py` in command line.
6. To check the database, perform the following steps:
  1. type in `psql` and then `create database tournament;`
  2. Press `Ctrl+D` to quit current psql and type in `psql tournament` to enter the database just entered.
  3. Type in `\i tournament.sql` to initialize all the tables and views predefined.
  4. `tournament_script.py` file may help set up some players and randomized match results for testing purpose.
