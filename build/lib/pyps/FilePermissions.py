#! /usr/bin/env python

class UserPermissions():
    """
    """
    @staticmethod
    def read(FileMode):
        return int(str(oct(FileMode))[-3]) in [4, 5, 6, 7]

    @staticmethod
    def write(FileMode):
        return int(str(oct(FileMode))[-3]) in [2, 3, 6, 7]

    @staticmethod
    def execute(FileMode):
        return int(str(oct(FileMode))[-3]) in [1, 3, 5, 7]

    @staticmethod
    def formatAsString(FileMode):
        user_read  = "-"
        user_write = "-"
        user_exec  = "-"
        if UserPermissions.read(FileMode):
            user_read = "r"
        if UserPermissions.write(FileMode):
            user_write = "w"
        if UserPermissions.execute(FileMode):
            user_exec = "x"
        return user_read + user_write + user_exec

class GroupPermissions():
    """
    """
    @staticmethod
    def read(FileMode):
        return int(str(oct(FileMode))[-2]) in [4, 5, 6, 7]

    @staticmethod
    def write(FileMode):
        return int(str(oct(FileMode))[-2]) in [2, 3, 6, 7]

    @staticmethod
    def execute(FileMode):
        return int(str(oct(FileMode))[-2]) in [1, 3, 5, 7]

    @staticmethod
    def formatAsString(FileMode):
        group_read  = "-"
        group_write = "-"
        group_exec  = "-"
        if GroupPermissions.read(FileMode):
            group_read = "r"
        if GroupPermissions.write(FileMode):
            group_write = "w"
        if GroupPermissions.execute(FileMode):
            group_exec = "x"
        return group_read + group_write + group_exec

class OtherPermissions():
    """
    """
    @staticmethod
    def read(FileMode):
        return int(str(oct(FileMode))[-1]) in [4, 5, 6, 7]

    @staticmethod
    def write(FileMode):
        return int(str(oct(FileMode))[-1]) in [2, 3, 6, 7]

    @staticmethod
    def execute(FileMode):
        return int(str(oct(FileMode))[-1]) in [1, 3, 5, 7]

    @staticmethod
    def formatAsString(FileMode):
        other_read  = "-"
        other_write = "-"
        other_exec  = "-"
        if OtherPermissions.read(FileMode):
            user_read = "r"
        if OtherPermissions.write(FileMode):
            user_write = "w"
        if OtherPermissions.execute(FileMode):
            user_exec = "x"
        return other_read + other_write + other_exec
