from dataclasses import dataclass
from enum import IntEnum


@dataclass
class Course:
    department: str
    course_numer: str

    @classmethod
    def from_string(cls, s: str):
        """
        String format: 4 letters of department and the rest of letters of course number

        e.g. COMP202, MATH470D2
        """

        return cls(s[:4], s[4:])


class Season(IntEnum):
    WINTER = 0
    SUMMER = 1
    FALL = 2

    @classmethod
    def from_char(cls, c: str):
        """
        W, S, F
        """

        if c == "W":
            return cls.WINTER
        elif c == "S":
            return cls.SUMMER
        elif c == "F":
            return cls.FALL
        else:
            raise ValueError("Char must be W, S or F")


@dataclass(order=True, frozen=True)
class Term:
    year: int
    season: Season

    @classmethod
    def from_string(cls, s: str):
        """
        String format: W2016, F2017, S2019, ...
        """

        return Term(int(s[1:]), Season.from_char(s[0]))


@dataclass
class Datapoint:
    course: Course
    term: Term
    course_average: int
