from abc import ABC
from os.path import isfile
import pandas as pd

class ExcelFrameManager(ABC):

    @property
    def origin(self):
        # return self.origin_name
        raise NotImplementedError('this manager is missing name of origin dataset')

    @property
    def name(self):
        # return self.origin_name
        raise NotImplementedError('this manager is missing name of saved frame')

    @property
    def use_only_origin(self):
        return False

    def get_path(self, origin=False):
        path = r'data_sources\excels\\'
        file = self.origin if origin else self.name
        return path + file + '.csv'

    def previously_extracted(self):
        return isfile(self.get_path())

    def _tranform(self, frame):
        return frame

    def extract(self):
        # frame = None
        if (not self.use_only_origin) and self.previously_extracted():
            frame = pd.read_csv(self.get_path())
        else:
            frame = pd.read_csv(self.get_path(origin=True))
            frame = self._tranform(frame)
            frame.to_csv(self.get_path())
        return frame
