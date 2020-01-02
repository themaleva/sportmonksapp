# sportmonksapp
Python app using Sportmonks API to process live scores &amp; updates

This app is being developed to make use of several APIs, namely:

- SportMonks:
  - A live football(soccer) score &amp; event API
  
- Twython:
  - A twitter python package to facilitate the auto-tweeting of scores and events during live matches

- TextLocal:
  - A paid for text messaging (SMS) service to update users/subscribers on the go
  
# Main Purpose
Retrieveal and processing of live football events in the Scottish Premier League (as it's free!) but will be built to handle any leagues offered by the SportMonks API service.

When finished, the app will run 24/7.

Process Outline:

1. 6am each morning check whether any fixtures are scheduled that day.
2. If no games are scheduled then sleep until 6am the following day.
3. If games are scheduled for 'today' then get fixtures from fixtures endpoint, storing the ID, team names (home vs away) and kick-off time - store these in a json file (names today's fixtures) for recovery purposes and keep in memory as a dictionary.
4. App to sleep until 1 minute before the next available kick-off time.
5. Once awake the app should check the in-play/live end-points for new events every 60 seconds.
6. Process each event if it hasn't been processed before and tweet update in real-time.
7. In each loop check for half-time status of matches. If status == HT then tweet half-time score and goalscorers & time scored.
8. In each loop also check for full-time status of matches. Repeat the above step but included final attendance and man of the match (if available)
9. If all games that day have FT status then post summary tweet of all results only (no goalscorers).
10. If no more games that day then delete json file and json.dump a new file with the results and events with 'todays' date as the filename.
11. App to sleep until 6am the following morning.



  
