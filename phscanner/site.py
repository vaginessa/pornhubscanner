#!/usr/bin/env python3
"""This module contains the PornHub class which holds the site
attributes and methods. It's meant to contain other sites stuff if the
program it's exapanded in the future.
"""

import re
from urllib.parse import unquote
from urllib.request import urlopen
from bs4 import BeautifulSoup


class PornHub(object):
    """Create a PornHub object to hold site attributes and methods

    Class private attributes:
        _home:  site homepage address
        _path:  video directory on the server
        _query: site query format
        _regex: regex needed to find direct video url in a page

    Instances argument:
        page (int): the site page number: count starts from 1 (homepage)
    """

    _home = 'http://www.pornhub.com'
    _path = '/video'
    _query = 'page='
    _tags = 'a', {'class': 'img'}
    _regex = re.compile(r'player[\w_]*\d{3}p = \\\'(http[:/\.\w\?=&]*)', re.I)

    def __init__(self, page=1):
        self.page = page

    def get_page_url(self):
        """Return the selected page url. Page 1 = homepage."""
        url = ''.join(
            [self._home, self._path, '?', self._query + str(self.page)])
        return url

    def _get_body(self):
        """Return a soup object created with given arguments."""
        with urlopen(self.get_page_url()) as html:
            sp = BeautifulSoup(html, 'html.parser')
            body = [i for i in sp.find_all(*self._tags) if i.has_attr('title')]
        return body

    def get_catalogue(self):
        """Return a dictionary of video titles and their pages."""
        video_page_urls = {}
        for i in self._get_body():
            video_page_urls[i.get('title')] = i.get('href')
        return video_page_urls

    def get_video_url(self, video_page_url):
        """Return the direct video url contained in the given page."""
        with urlopen(self._home + video_page_url) as html:
            match = re.search(self._regex, str(html.read()))
        video_url = unquote(re.sub('&amp', '', match.group(1)))
        return video_url
