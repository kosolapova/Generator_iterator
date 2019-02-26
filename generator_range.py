def gen_range(stop, start=0, step=1):
    if isinstance(stop, int) and isinstance(start, int) and isinstance(step, int):
        current = start
        if start < stop and step > 0:
            while current < stop:
                yield current
                current += step
        elif start > stop and step < 0:
            while current > stop:
                yield current
                current += step
    else:
        raise TypeError('gen_range function requires integers as arguments')

