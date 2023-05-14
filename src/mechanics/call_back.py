class call_back:
    """class, used so functions can easily be wrapped and called back
    Atributes:
        function: function to be called
        args: arguments for the funtion
        kwargs: keyword arguments for the funtion
    """
    def __init__(self,function,*args, **kwargs):
        self.function = function
        self.args=args
        self.kwargs= kwargs
    def call(self):
        """calls the function
        """
        self.function(self.args,)