from MemberofCouncil import MemberofCouncil

class ChairmanofCouncil(MemberofCouncil):
    def __init__(self, fullname, birthday, group, sector):
        self._sector = sector
        self._fullname = fullname
        self._birthdate = birthday
        self._group = group

    