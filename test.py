from time import perf_counter


class Timer:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Function {self.fn.__name__} finish working in {finish - start} seconds')
        return result


def stepen(num, stepen):
    return num ** stepen
