from python_loc_counter import LOCCounter
import os, shutil, stat
from functools import reduce

def on_rm_error( func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod( path, stat.S_IWRITE )
    os.unlink( path )

class AnalisysRepository:
    def __init__(self, urlRepository):
        self.urlRepository = urlRepository
        self.path = './temp'

    def _cloneRepository(self):
        cloneCommand = f"git clone {self.urlRepository} {self.path}"
        os.system(cloneCommand)

    def _removeRepository(self):
        shutil.rmtree(self.path, onerror= on_rm_error)

    def _sum_loc_data(self, a, b):
        c = {
            'source_loc': a['source_loc'] + b['source_loc'],
            'single_comments_loc': a['single_comments_loc'] + b['single_comments_loc'],
            'single_docstring_loc': a['single_docstring_loc'] + b['single_docstring_loc'],
            'double_docstring_loc': a['double_docstring_loc'] + b['double_docstring_loc'],
            'total_comments_loc': a['total_comments_loc'] + b['total_comments_loc'],
            'blank_loc': a['blank_loc'] + b['blank_loc'],
            'total_line_count': a['total_line_count'] + b['total_line_count']
        }
        return c

    def _analisysRepository(self):
        analisys = list()
        for dirName, subdirList, fileList in os.walk(self.path):
            for file in fileList:
                filePath = os.path.join(dirName, file)
                print('Analyzing' + filePath)
                try:
                    counter = LOCCounter(filePath)
                    loc_data = counter.getLOC()
                    analisys.append(loc_data)
                except: 
                    print('Couldn\'t analyze the file ' + filePath)     
        return reduce(lambda a, b: self._sum_loc_data(a, b), analisys)

    def analyze(self):
        self._cloneRepository()
        result = self._analisysRepository()
        self._removeRepository()
        return result