class Maybe:
    def __init__(self):
        pass

    def is_just(self):
        return self.__class__ == Just

    def is_nothing(self):
        return self.__class__ == Nothing

    @staticmethod
    def from_just(_maybe):
        if _maybe.is_just():
            return _maybe.value
        else:
            raise Exception('Maybe#from_just called with Maybe#Nothing')

    @staticmethod
    def from_maybe(_maybe, default):
        if _maybe.is_nothing():
            return default
        else:
            return _maybe.value

class Nothing(Maybe):
    def __init__(self):
        pass

    def __repr__(self):
        return 'Maybe#Nothing()'

class Just(Maybe):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Maybe#Just(%s)' % self.value
