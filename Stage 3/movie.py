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

from video import Video

class Movie(Video):
 """This class representing a movie object."""

    def __init__(self, movie_title, movie_description, movie_poster_image_url, movie_trailer_youtube_url):
        """Initiate the movie instance.

        Args:
            movie_title: A string representing the movie title.
            movie_description: A string representing the movie description.
            movie_poster_image_url: A string representing the movie poster image url.
            movie_trailer_youtube_url: A string representing the movie trailer youtube url.

        Returns:
            Nothing.
        """
        Video.__init__(self, movie_title, movie_description, movie_poster_image_url, movie_trailer_youtube_url)
        self.storyline = "movie_storyline"
        self.director = "Unknown"
        self.writers = "writers"
        self.stars = "stars"
        self.taglines = "taglines"
        self.genres = "genres"
        self.country = "country"
        self.language = "language"
        self.release_date = "release_date"
        self.runtime = "runtime"

    def print_info(self):
        """Printing the movie info.

        Args:
            None.

        Returns:
            Nothing.
        """
        print("===============START======================")
        print("title: " + self.title)
        print("description: " + self.description)
        print("poster_image_url: " + self.poster_image_url)
        print("trailer_youtube_url: " + self.trailer_youtube_url)
        print("storyline: " + self.storyline)
        print("director: " + self.director)
        print("writers: " + self.writers)
        print("stars: " + self.stars)
        print("taglines: " + self.taglines)
        print("genres: " + self.genres)
        print("country: " + self.country)
        print("language: " + self.language)
        print("release_date: " + self.release_date)
        print("runtime: " + self.runtime)
        print("===============END======================")