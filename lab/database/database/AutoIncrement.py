class AutoIncrement:

    @staticmethod
    def auto_increment(start_in=0, step_in=1):
        i = start_in
        while True:
            yield i
            i += step_in
