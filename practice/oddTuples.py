# Write a procedure called oddTuples, which takes a tuple as input, and
# returns a new tuple as output, where every other element of the input tuple
#  is copied, starting with the first one. So if test is the tuple
# ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input
# would return the tuple ('I', 'a', 'tuple').


def odd_tuples(a_tup):
    new = ()
    for i in range(len(a_tup)):
        if i % 2 == 0:
            new = new + (a_tup[i],)
    return new


test = ('I', 'am', 'a', 'test', 'tuple')
ret_test = odd_tuples(test)
print(ret_test)
