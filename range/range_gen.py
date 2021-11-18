def range(start, end: int = None, step=1):
    if end is None:
        start, end = 0, start

    i = start
    while i < end:
        yield i
        i += step
