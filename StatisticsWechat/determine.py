import re
import jieba


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
            raise ValueError("无法正则")
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

    # @classmethod
    def getNumber(self):
        '''
        过滤剩下数字，并且剩下排序返回数组
        '''
        # pass
        m = self.dealInfo(self.content)
        while True:
            num = re.sub("\D", " ", m)
            c = num.strip()
            new = jieba.__lcut(c)
            while ' ' in new:
                new.remove(' ')
        return new

    def getLocation(self):
        '''
        处理文字部分，返回文字数组
        '''
        # pass
        m = self.dealInfo(self.content)
        while True:
            num = re.sub("\d", " ", m)
            c = num.strip()
            word = jieba.__lcut(c)
            """
            待处理一些图文符号
            """

            while ' ' in word:
                word.remove(' ')
        return word

    def sortNum(self, num):
        """
        处理剩下数字的结果，并且排序，无值设0
        功能:
            182 97年 28  ，识别判断输出年龄和身高
            判断“92快93”这儿类字眼，以
        ------
        stature | age

        """
        # pass
        newNum = []
        if isinstance(num, list):
            Sort = sorted(num, reverse=True)
            if 0 <= len(num) <= 2:
                if len(num) == 0:
                    num.extend([0, 0])
                elif len(num) == 1:
                    """ 判断第一个数是哪一个 """
                    if num[0] > 100:
                        num.extend([0])
                        return num
                    elif 80 < num[0] < 100:
                        num.insert(0, 0)
                        return num
                    elif 10 < num[0] < 30:
                        num.insert(0, 0)
                        return num
                    elif 0 <= num[0] <= 10:
                        print("erro")
                    else:
                        raise ValueError("出错")
                elif len(num) == 2:
                    if num[0] > 100:
                        if 80 < num[1] < 100:
                            return num
                        elif 10 < num[1] < 30:
                            return num
                    elif 80 < num[0] < 100:
                        """ 过滤两个90 """
                        if 80 < num[1] < 100:
                            num.pop()
                            num.insert(0, 0)
                            return num
                        elif 100 <= num[1] <= 300:
                            num[0], num[1] = num[1], num[0]
                            return num
                        elif 10 < num[1] < 30:
                            num.pop(0)
                            num.extend([0])
                            
                            return num
                        else:
                            # num.pop()
                            # num.insert(0, 0)
                            # return num
                            raise ValueError("第一个数字是出生年月，第二个数字无法判别")
                    elif 10 < num[0] < 30:
                        """ 只有年龄 """
                        num.pop()
                        num.insert(0, 0)
                        return num
                else:
                    raise ValueError("超过两个数字")
            elif len(num) == 3:
                num.pop()
                self.sortNum(num)
            else:
                raise ValueError("输入不对")
        else:
            raise ValueError("不是数组")
        return num

        # elif num[0] > 100:
        #     newNum.append(num[0])
        # else:
        #     if 70 < num[0] < 100:
        #         newNum.append(num[0])  """ 生日年份 """
        #     else:
        #         newNum.append([num[0]]) """ 年龄 """

    def sortWord(self, word):
        """  
        处理剩下文字的结果，并排序列,
        功能:
            识别文字地点，其他文字，英语
            例如：北京  我就是我  cnncncn， 提取地点

        ------
        location

        """
        pass

    def end(self):
        '''  
        处理所有结果，并且返回数组
        '''
        # pass
        number = self.getNumber()
        Word = self.getLocation()
        pass
