#----------------------------------
#
# IPND Stage 3 Final Project
#
#----------------------------------
# KS81 Movie Trailers
#
# Developer: Kenneth Soerensen
# 
# MIT License
#
# Copyright (c) 2016 Kenneth Soerensen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#----------------------------------

from movie import Movie
import fresh_tomatoes

# Movies
# Arrival
arrival = Movie("Arrival",
                "A linguist is recruited by the military to assist in translating alien communications.",
                "./images/arrival.jpg",
                "https://www.youtube.com/watch?v=ZLO4X6UI8OY")

arrival.storyline = "When mysterious spacecraft touch down across the globe, an elite team - led by expert linguist Louise Banks - is brought together to investigate. As mankind teeters on the verge of global war, Banks and the team race against time for answers - and to find them, she will take a chance that could threaten her life, and quite possibly humanity."

arrival.director = "Denis Villeneuve"
arrival.writers = "Eric Heisserer (screenplay), Ted Chiang (based on the story \"Story of Your Life\" written by)"
arrival.stars = "Amy Adams, Jeremy Renner, Forest Whitaker"
arrival.taglines = "Why are they here?"
arrival.genres = "Drama | Mystery | Sci-Fi | Thriller"
arrival.country = "USA"
arrival.language = "English"
arrival.release_date = "11 November 2016 (Norway)"
arrival.runtime = "116 min"

# Kong: Skull Island
kong_skull_island = Movie("Kong: Skull Island",
                          "An action/adventure story centered on King Kong's origins.",
                          "./images/KongSkullIsland.jpg",
                          "https://www.youtube.com/watch?v=h9y6oPka3us")

kong_skull_island.storyline = "An action/adventure story centered on King Kong's origins."
kong_skull_island.director = "Jordan Vogt-Roberts"
kong_skull_island.writers = "Dan Gilroy (screenplay), John Gatins (screenplay), Max Borenstein (screenplay), Derek Connolly (screenplay)"
kong_skull_island.stars = "Brie Larson, Tom Hiddleston, Toby Kebbell"
kong_skull_island.taglines = "Awaken the King"
kong_skull_island.genres = "Action | Adventure | Fantasy | Sci-Fi"
kong_skull_island.country = "USA"
kong_skull_island.language = "English"
kong_skull_island.release_date = "10 March 2017	(Norway)"
kong_skull_island.runtime = "Unknown"

# Life on the Line
life_on_the_line = Movie("Life on the Line",
                         "A crew of men who do the high-wire work of fixing the electrical grid are hit by a sudden deadly storm.",
                         "./images/LifeOnTheLine.jpg",
                         "https://www.youtube.com/watch?v=nEz8Z_G8SBk")

life_on_the_line.storyline = "LIFE ON THE LINE is a riveting action thriller and family drama centered on Beau (John Travolta), his beloved niece Bailey (Kate Bosworth) and the hardworking men who risk their lives to work \"on the line\" and keep the electric grid running. These unsung heroes brave raging storms and dangerously dizzying heights in their dedication to keeping the populace safe. Toiling hundreds of feet in the air on wires carrying as much as 500,000 volts of electricity, tragedy is often inches away. Haunted by the electrocution death of his brother, Beau is devoted to Bailey and determined to see her go off to college and away from the life of linemen. Bailey has other plans, which include the strapping second-generation lineman Duncan (Devon Sawa), whom Beau despises. A deadly tempest is brewing and headed straight to their Texas town. Beau, Duncan and a legion of linemen are thrust into the eye of the storm and must face down impending disaster to keep their community connected. This compelling ..."
life_on_the_line.director = "David Hackl"
life_on_the_line.writers = "Primo Brown, Peter I. Horton, Marvin Peart, Dylan Scott"
life_on_the_line.stars = "John Travolta, Kate Bosworth, Devon Sawa"
life_on_the_line.taglines = "Courage. Risk. Sacrifice."
life_on_the_line.genres = "Action | Drama"
life_on_the_line.country = "USA"
life_on_the_line.language = "English"
life_on_the_line.release_date = "18 November 2016 (USA)"
life_on_the_line.runtime = "97 min"

# Hacksaw Ridge
hacksaw_ridge = Movie("Hacksaw Ridge",
                      "WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people, and becomes the first man in American history to win the Medal of Honor without firing a shot.",
                      "./images/HacksawRidge.jpg",
                      "https://www.youtube.com/watch?v=9BqgHYLvHIE")

hacksaw_ridge.storyline = "WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people, and becomes the first man in American history to win the Medal of Honor without firing a shot."
hacksaw_ridge.director = "Mel Gibson"
hacksaw_ridge.writers = "Robert Schenkkan (screenplay), Andrew Knight (screenplay)"
hacksaw_ridge.stars = "Andrew Garfield, Sam Worthington, Luke Bracey"
hacksaw_ridge.taglines = "Based on the incredible true story. | When the order came to retreat, one man stayed. | One of the greatest heroes in America history never fired a bullet."
hacksaw_ridge.genres = "Drama | History | War"
hacksaw_ridge.country = "Australia | USA"
hacksaw_ridge.language = "English"
hacksaw_ridge.release_date = "9 December 2016 (Norway)"
hacksaw_ridge.runtime = "139 min"

# The Accountant
the_accountant = Movie("The Accountant",
                       "As a math savant uncooks the books for a new client, the Treasury Department closes in on his activities and the body count starts to rise.",
                       "./images/TheAccountant.jpg",
                       "https://www.youtube.com/watch?v=DBfsgcswlYQ")

the_accountant.storyline = "Christian Wolff is a math savante with more affinity for numbers than people. Behind the cover of a small-town CPA office, he works as a freelance accountant for some of the world's most dangerous criminal organizations. With the Treasury Department's Crime Enforcement Division, run by Ray King, starting to close in, Christian takes on a legitimate client: a state-of-the-art robotics company where an accounting clerk has discovered a discrepancy involving millions of dollars. But as Christian uncooks the books and gets closer to the truth, it is the body count that starts to rise."
the_accountant.director = "Gavin O'Connor"
the_accountant.writers = "Bill Dubuque"
the_accountant.stars = "Ben Affleck, Anna Kendrick, J.K. Simmons"
the_accountant.taglines = "Calculate your choices."
the_accountant.genres = "Action | Crime | Drama | Thriller"
the_accountant.country = "USA"
the_accountant.language = "English"
the_accountant.release_date = "2 December 2016 (Norway)"
the_accountant.runtime = "128 min"

# Jack Reacher: Never Go Back
jack_reacher_never_go_back = Movie("Jack Reacher: Never Go Back",
                                   "Jack Reacher must uncover the truth behind a major government conspiracy in order to clear his name. On the run as a fugitive from the law, Reacher uncovers a potential secret from his past that could change his life forever.",
                                   "./images/JackReacherNeverGoBack.jpg",
                                   "https://www.youtube.com/watch?v=MHiqfKqjZio")

jack_reacher_never_go_back.storyline = "Jack Reacher must uncover the truth behind a major government conspiracy in order to clear his name. On the run as a fugitive from the law, Reacher uncovers a potential secret from his past that could change his life forever."
jack_reacher_never_go_back.director = "Edward Zwick"
jack_reacher_never_go_back.writers = "Richard Wenk (screenplay), Edward Zwick (screenplay), Marshall Herskovitz (screenplay), Lee Child (book)"
jack_reacher_never_go_back.stars = "Tom Cruise, Cobie Smulders, Aldis Hodge"
jack_reacher_never_go_back.taglines = "Never give in. Never give up. Never go back. | Justice is Coming. | Tom Cruise is Jack Reacher. | Justice is Coming in IMAX. | Never give in. | Never give up."
jack_reacher_never_go_back.genres = "Action | Adventure | Crime | Mystery | Thriller"
jack_reacher_never_go_back.country = "China | USA"
jack_reacher_never_go_back.language = "English"
jack_reacher_never_go_back.release_date = "28 October 2016 (Norway)"
jack_reacher_never_go_back.runtime = "118 min"

# Making the website
media = [arrival, kong_skull_island, life_on_the_line, hacksaw_ridge, the_accountant, jack_reacher_never_go_back]
fresh_tomatoes.open_movies_page(media)