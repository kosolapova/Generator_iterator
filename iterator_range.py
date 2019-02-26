class IterRange:
    def __init__(self, stop, start=0, step=1):
        if isinstance(stop, int) and isinstance(start, int) and isinstance(step, int):
            self.current = start
            self.stop = stop
            self.step = step
            if self.stop > self.current and self.step > 0:
                self.direct = True
            elif self.stop < self.current and self.step < 0:
                self.direct = False
            else:
                self.direct = None
        else:
            raise TypeError('IterRange class requires integers as arguments')

    def __iter__(self):
        return self

    def __next__(self):
        if self.direct is True:
            if self.current < self.stop:
                self.current += self.step
                return self.current - self.step
            else:
                raise StopIteration
        elif self.direct is False:
            if self.current > self.stop:
                self.current += self.step
                return self.current - self.step
            else:
                raise StopIteration
        else:
            raise StopIteration

