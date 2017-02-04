import random
from tournament import connect, reportMatch
from tournament_test import testDelete

the_players = [(1, 'Jeff'),
               (2, 'Miki'),
               (3, 'Stitch'),
               (4, 'JT'),
               (5, 'Judith'),
               (6, 'Nick'),
               (7, 'Lara'),
               (8, 'Nate')]

def registerPlayerwithID(player_id, name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (id, name) VALUES (%s, %s)", (player_id, name))
    DB.commit()
    DB.close

def createRandomMatches(player_list, num_matches):
    num_players = len(player_list)
    for i in xrange(num_matches):
        print 'match %s' % (i + 1)
        player1_index = random.randint(0, num_players - 1)
        player2_index = random.randint(0, num_players - 1)
        if player1_index == player2_index:
            player2_index = (player1_index + 1) % num_players

        winner_id = player_list[player1_index][0]
        winner_name = player_list[player1_index][1]
        loser_id = player_list[player2_index][0]
        loser_name = player_list[player2_index][1]

        reportMatch(winner_id, loser_id)
        print "%s (id = %s) beats %s (id = %s)" % (winner_name,
                                                   winner_id,
                                                   loser_name,
                                                   loser_id)

def setupPlayersandMatches():
    testDelete()
    for player in the_players:
        registerPlayerwithID(player[0], player[1])
    createRandomMatches(the_players, 100)

if __name__ ==  '__main__':
    setupPlayersandMatches()