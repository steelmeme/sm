class Maybe:
    def __init__(self):
        pass

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
