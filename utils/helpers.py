class Helper:

    def __init__(self, page):
        self.page = page

    def stringToBoolean(self, stringVal: str) -> bool:
        truthyValues = ('true', 'yes', '1', 'y')
        falsyValues = ('false', 'no', '0', 'n')
        stringVal = stringVal.strip().lower()
        if stringVal in truthyValues:
            return True
        elif stringVal in falsyValues:
            return  False
        else:
            raise ValueError(f"Cannot convert {stringVal} to boolean")