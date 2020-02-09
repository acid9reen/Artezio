''''Student class implementation'''


class Student:
    ''''Student class implementation'''

    try_num = 3
    exam_mark = 0

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.labs = {i: [0, 0] for i in range(conf["lab_num"])}

    def make_lab(self, mark, lab_num=None):
        '''Make lab'''

        if lab_num not in self.labs.keys():
            return self

        if lab_num is None:
            for key in self.labs.keys():
                if (lab := self.labs[key])[1] == 0:
                    if mark <= self.conf["lab_max"] \
                            and lab[1] < self.try_num:
                        lab[0] = mark
                        lab[1] += 1
                        break

            return self

        if (lab := self.labs[lab_num])[1] < self.try_num \
                and mark <= self.conf["lab_max"]:
            lab[0] = mark
            lab[1] += 1

        return self

    def make_exam(self, mark):
        '''Make exam'''

        if mark <= self.conf["exam_max"]:
            self.exam_mark = mark

        return self

    def is_certified(self):
        '''Return total mark and True if
            the student scored the required mark else
            return total mark and False'''

        total_mark = 0
        max_mark = (self.conf["lab_max"] * self.conf["lab_num"]
                    + self.conf["exam_max"])

        for value in self.labs.values():
            total_mark += value[0]

        if (coef := total_mark / max_mark) < self.conf["k"]:
            return coef, False

        return coef, True
