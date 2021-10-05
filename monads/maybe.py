class Maybe:
    def __init__(self):
        pass

    @staticmethod
    def is_just(_maybe):
        return _maybe.__class__ == Just

    @staticmethod
    def is_nothing(_maybe):
        return _maybe.__class__ == Nothing

    @staticmethod
    def from_just(_maybe):
        if Maybe.is_just(_maybe):
            return _maybe.value
        else:
            raise Exception('Maybe#from_just called with Maybe#Nothing')

    @staticmethod
    def from_maybe(_maybe, default):
        if Maybe.is_nothing(_maybe):
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
