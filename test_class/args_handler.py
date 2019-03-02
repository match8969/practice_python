"""
Reference :: https://stackoverflow.com/questions/141545/how-to-overload-init-method-based-on-argument-type

lass MyData:
...     def __init__(self, data):
...         "Initialize MyData from a sequence"
...         self.data = data
...
...     @classmethod
...     def fromfilename(cls, filename):
...         "Initialize MyData from a file"
...         data = open(filename).readlines()
...         return cls(data)
...
...     @classmethod
...     def fromdict(cls, datadict):
...         "Initialize MyData from a dict's items"
...         return cls(datadict.items())
...
 MyData([1, 2, 3]).data
[1, 2, 3]
 MyData.fromfilename("/tmp/foobar").data
['foo\n', 'bar\n', 'baz\n']
 MyData.fromdict({"spam": "ham"}).data
[('spam', 'ham')]

"""

class ArgsHandler(object):
    list_args = []

    def __init__(self, list_args):
        self.list_args = list_args

    def count_args(self):
        return len(self.list_args)

    def to_dict_parsedfile(self):
        dict = {}
        # TODO Check the args and return the detail
        # IMAGE   dict = {args1: .csv, args2: txtfile, args3: dir}

        return


    # test
    def show_args(self):
        print('list_args is......')
        print(self.list_args)