class call_back:
    def __init__(self,function,*args, **kwargs):
        self.function = function
        self.args=args
        self.kwargs= kwargs
    def call(self):
        self.function(self.args,)