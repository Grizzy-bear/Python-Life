import re


class Info(object):
    def __init__(self, content):
        self.content = content

    @property
    def dealInfo(self, String):
        # pass
        '''  
        去除多于符号，后续分类处理文字和数字
        '''
        try:
            _dealString = re.sub("[\!\%\[\]\,\。\()\-\~]", " ", String)
        except expression as identifier:
            pass
        return _dealString

    @dealInfo.setter
    def dealInfo(self, value):
        '''  
        判断去除非数字文字的符号后判断是否有属性
        '''
        if value == None:
            raise ValueError("值没有属性")
        else:
            _dealString = value


    def getNumber(self):
        '''  
        过滤剩下文字，并且剩下排序返回数组
        '''
        pass

    def getLocation(self):
        ''' 
        处理文字部分，返回文字数组   
        '''
        pass
    
    def end(self):
        '''  
        处理所有结果，并且返回数组
        '''
        pass
