import  time


class Timer(object):
    def __int__(self,verbose=False):
        self.verbose = verbose

    def _enter_(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.secs = self.end - self.start
        self.millis = self.secs * 1000
        if self.verbose:
            print('elapsed time: {0:f} ms'.format(self.millis))