import re
class FemapRsuBeam:
    def __init__(self, seysmik, wind_y, wind_x):
        '''
        объект при инициализации считывает 3 файла в свои списки аттрибуты,
        затем он передается для итераций объекту класса WForeach из пакета WorkSheetsForeach,
        итерирующему список xls файлов
        :param seysmik: исходный файл данных сейсмических усилий
        :param wind_y: исходный файл данных усилий от загружения Ветер Y
        :param wind_x: исходный файл данных усилий от загружения Ветер Х
        пример вызова:
        from FeemapForces.FeemapForces import FemapRsuBeam as fb
        test = fb(seysmik="G:/temp/analiz/seysmik", wind_x="G:/temp/analiz/wind_x", wind_y="G:/temp/analiz/wind_y")
        test.numbers(["1908", "1907"])
        '''
        self.seysmik = seysmik  # для целей отладки
        self.wind_y = wind_y
        self.wind_x = wind_x
        self.mLinesSm = self.openReadClose(seysmik)
        self.mLinesWy = self.openReadClose(wind_y)
        self.mLinesWx = self.openReadClose(wind_x)

        
    def openReadClose(self, name):
        f = open(name, "r")
        m = f.readlines()
        f.close()
        return m
        
    def numbers(self, mArg):
        '''
        возвращает массивы усилия для ряда КЕ, для всех их сечений
        :param mArg:
        :return:
        '''
        pat = "(\d\.\d+E[-+]\d+)\s+"
        self.mnSm = []; self.mnWx = []; self.mnWy = []
        for item in mArg:
            pass
            searchPat = "\s+" + item + "\s+\d+\s+\d\s+" + pat + pat + pat + pat + pat + pat
            fPat = re.compile(searchPat)
            self.mnSm.append(self.eachFileN(self.mLinesSm, fPat))
            self.mnWy.append(self.eachFileN(self.mLinesWy, fPat))
            self.mnWx.append(self.eachFileN(self.mLinesWx, fPat))
            return [self.mnWy, self.mnWx, self.mnSm]


    def eachFileN(self, LinesInFile, fPat):
        '''
        Метод итерирует усилия из отдельного файла (одна группа усилий)
        :param LinesInFile: массив усилий
        :param fPat: скомпилированное рег.выражение
        :return: возвращает массив 6-ти видов усилий для отдельного КЕ, для каждого из их сечений
        '''
        m = []
        for i in LinesInFile:
            f = re.search(fPat, i)
            if f != None:
                n1 = f.group(1)
                n2 = f.group(2)
                n3 = f.group(3)
                n4 = f.group(4)
                n5 = f.group(5)
                n6 = f.group(6)
                m.append([n1,n2,n3,n4,n5,n6]) # возвращаемый массив содержит усилия femap для каждого сечения (массив массивов)
        return m

class FemapRsuBraces(FemapRsuBeam):
    def numbers(self, mArg):
        '''
        возвращает массивы усилия для ряда КЕ, для всех их сечений
        :param mArg:
        :return:
        '''
        pat = "(\d\.\d+E[-+]\d+)\s+"
        self.mnSm = []; self.mnWx = []; self.mnWy = []
        for item in mArg:
            pass
            searchPat = "\s+" + item + "\s+\d+\s+" + pat + pat
            fPat = re.compile(searchPat)
            self.mnSm.append(self.eachFileN(self.mLinesSm, fPat))
            self.mnWy.append(self.eachFileN(self.mLinesWy, fPat))
            self.mnWx.append(self.eachFileN(self.mLinesWx, fPat))
            return [self.mnWy, self.mnWx, self.mnSm]
    def eachFileN(self, LinesInFile, fPat):
        '''
        Метод итерирует усилия из отдельного файла (одна группа усилий)
        :param LinesInFile: массив усилий
        :param fPat: скомпилированное рег.выражение
        :return: возвращает массив 2-х видов усилий для отдельного КЕ, для каждого из их сечений
        '''
        m = []
        for i in LinesInFile:
            f = re.search(fPat, i)
            if f != None:
                n1 = f.group(1)
                m.append([n1]) # возвращаемый массив содержит усилия femap
        return m