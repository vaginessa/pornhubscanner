"""
This module contains the Download class which creates the thread
used to manage the download of the selected video without hanging the
main interface.
"""

import urllib.request
from PyQt4.QtCore import pyqtSignal, QObject


class Download(QObject):
    """
    A class to create a 'downloader' object meant to be run in a
    separate QThread. The entry point is the 'start_process' method. The
    class also contains two signals:

        reportInfo: carries an int and is emitted on download progress
        finished: emitted when download is finished.
    """
    report = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, video_url, video_title):
        super().__init__()
        self.video_url = video_url
        self.video_title = video_title + '.mp4'
        self.exiting = False

    def _report(self, blocknum, blocksize, totalsize):
        """
        Report hook for the download, emits a signal with downloaded
        percentage value.
        """
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percentage = readsofar * 100 / totalsize
            self.report.emit(percentage)

    def start_process(self):
        """Entry point for the object, manages the download."""
        block_size = 4096
        written_data = 0
        blocks_counter = 0

        with urllib.request.urlopen(self.video_url) as temp:
            headers = temp.info()
            totalsize = int(headers['Content-Length'])
            with open(self.video_title, 'wb') as file_to_write:
                while written_data < totalsize and self.exiting is False:
                    file_to_write.write(temp.read(block_size))
                    written_data += block_size
                    blocks_counter += 1
                    self._report(blocks_counter, block_size, totalsize)
        self.finished.emit()
