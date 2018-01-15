This is a texas holdem pokergame written in python.
The game is very buggy right now, but somewhat functional.

This was my first attempt at using python sockets to make a multiplayer game.
As of now it has been tested using separate terminals with localhost.

*** Warning, code is a mess ***

CURRENT KNOWN ISSUES: 
  - Game hasn't been tested outside of localhost
  - Players quitting midgame cause issues
  - Game only works with 2 players
  - Player with 0 chips remaining can still make moves
  - Players unable to match full bets are unaccounted for
  - All players forced to ante up 5 chips each hand
  - Cards are not hidden on fold
