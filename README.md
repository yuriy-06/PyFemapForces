Этот пакет предназначен для вывода усилий из текстовых файлов программы FeMap для серии КЕ балок, колонн и связей.

Пример использования:
```
from FemapForces.FemapForces import FemapRsuBeam as fb  # or
from FemapForces.FemapForces import FemapRsuBraces as fbrace
test = fb(seysmik="G:/temp/analiz/seysmik", wind_x="G:/temp/analiz/wind_x", wind_y="G:/temp/analiz/wind_y")
testBrace = fbrace(seysmik="G:/temp/analiz/seysmik", wind_x="G:/temp/analiz/wind_x", wind_y="G:/temp/analiz/wind_y")
test.numbers(["1908", "1907"])
testBrace.numbers(["1915", "1927"])
```