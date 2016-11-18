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

import webbrowser

class Video():
"""This class representing a video object."""

    def __init__(self, video_title, video_description, video_poster_image_url, video_trailer_youtube_url):
        """Initiate the movie instance.

        Args:
            video_title: A string representing the video title.
            video_description: A string representing the video description.
            video_poster_image_url: A string representing the video poster image url.
            video_trailer_youtube_url: A string representing the video trailer youtube url.

        Returns:
            Nothing.
        """
        self.title = video_title
        self.description = video_description
        self.poster_image_url = video_poster_image_url
        self.trailer_youtube_url = video_trailer_youtube_url

    def print_info(self):
        """Printing the video info.

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
        print("===============END======================")

    def show_trailer(self):
        """Open the youtube url in the default web browser.

        Args:
            None.

        Returns:
            Nothing.
        """
        webbrowser.open(self.trailer_youtube_url)