import urllib.request
from PyQt4.QtCore import pyqtSignal, QObject


class DownloadProcess(QObject):
    finished = pyqtSignal()
    report = pyqtSignal(int)

    def __init__(self, url, title):
        super().__init__()
        self.url = url
        self.title = title + '.mp4'
        self.exiting = False

    def _report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percentage = readsofar * 100 / totalsize
            self.report.emit(percentage)

    def start_process(self):
        block_size = 4096
        written_data = 0
        blocks_counter = 0

        with urllib.request.urlopen(self.url) as temp:
            headers = temp.info()
            totalsize = int(headers['Content-Length'])
            with open(self.title, 'wb') as file_to_write:
                while written_data < totalsize and self.exiting is False:
                    file_to_write.write(temp.read(block_size))
                    written_data += block_size
                    blocks_counter += 1
                    self._report(blocks_counter, block_size, totalsize)
        self.finished.emit()
