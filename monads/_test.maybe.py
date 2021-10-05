from maybe import *

jval = 1
just = Just(jval)

assert Maybe.from_just(just) == jval

nothing = Nothing()
dvalue = 'default'
res = Maybe.from_maybe(nothing, dvalue)
assert res == dvalue
