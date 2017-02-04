-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players ( id SERIAL PRIMARY KEY,
                       name TEXT );

CREATE TABLE matches ( id SERIAL PRIMARY KEY,
                       winner INTEGER REFERENCES players (id),
                       loser INTEGER REFERENCES players (id) );

CREATE VIEW win_total AS SELECT players.name, count(matches.winner) AS win_total
                         FROM players LEFT JOIN matches ON players.id = matches.winner
                         GROUP BY players.name ORDER BY win_total DESC;

CREATE VIEW match_total AS SELECT players.name, count(matches.id) AS match_total
                           FROM players LEFT JOIN matches ON players.id = matches.winner OR players.id = matches.loser
                           GROUP BY players.name ORDER BY match_total DESC;
