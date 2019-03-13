#!/usr/bin/python3
# -*- coding: utf-8 -*-


class CheckDummy:
    def __init__(self):
        pass

    def perform(self) -> int:
        return 0  # 1


if __name__ == "__main__":
    INST = CheckDummy()
    RET = INST.perform()
    exit(RET)
