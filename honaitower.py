#!/bin/python3

import os
import sys

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class HonaiTower():

    def __init__(self,size):

        self.Stacks = []
        self.size = size
        self.totalMovement = 0

        for i in range(3):
            self.Stacks.append(Stack(i))

        for i in range(size,0,-1):
            self.Stacks[0].disks.append(Disk(i))

        self.start()

    def get_tower(self):

        for i in range(3):
            if self.Stacks[i].is_empty():
                continue
            else :
                self.Stacks[i].get_Stack()

    def start(self):
        self.get_tower()
        self.move_disk()

    def move_disk(self):

        print(colors.HEADER+"++++++++++++++++++++++++++++++++++++++++++++++++"+colors.ENDC)

        source = int(input(colors.OKBLUE+"Hangi Stackdaki diski kaydirmak istiyorsunuz: "+colors.ENDC))
        if source > 2 or source < 0:
            print(colors.FAIL+"Hata: Yanlıs Stack secimi"+ colors.ENDC)
            return self.move_disk()

        if self.Stacks[source].is_empty() :
            print(colors.FAIL+"Hata: Kaynak Stackda disk yok"+ colors.ENDC)
            return self.move_disk()

        target = int(input(colors.OKBLUE+"Hangi Stacka kaydirmak istiyorsunuz: "+colors.ENDC))

        if target > 2 or target < 0:
            print(colors.FAIL+"Hata: Yanlıs Stack secimi"+ colors.ENDC)
            return self.move_disk()

        if self.Stacks[target].is_empty():
            self.Stacks[target].disks.append(self.Stacks[source].disks.pop())
        elif self.Stacks[source].top()>self.Stacks[target].top():
            print(colors.FAIL+"Hata: Yer değiştirdiğiniz disk hedef stackdaki diskten kucuk olmali!"+ colors.ENDC)
            return self.move_disk()
        else :
            self.Stacks[target].disks.append(self.Stacks[source].disks.pop())

        self.totalMovement = self.totalMovement + 1
        self.is_win()
        os.system('clear')
        print(colors.OKGREEN+"\nBasarili Adım: ",str(source)," --> ",str(target),colors.ENDC)
        print(colors.WARNING+"Total Movement: ",str(self.totalMovement),"\n",colors.ENDC)
        self.get_tower()
        return self.move_disk()

    def is_win(self):
        print('QQQQ')
        if self.Stacks[0].is_empty() and self.Stacks[1].is_empty() and self.Stacks[2].get_size() == self.size:
            print('YYYYY')
            os.system('clear')
            print(colors.HEADER+"Tebrikler! Kazandiniz"+colors.ENDC)
            print(colors.OKGREEN+"Total Movement: ",str(self.totalMovement),"\n",colors.ENDC)
            self.get_tower()
            exit()

class Stack():

    def __init__(self,name):
        self.name = str(name)

        self.disks= []

    def __str__(self):

        return self.name + ". Stack"

    def get_size(self):
        return len(self.disks)

    def is_empty(self):
        return False if self.get_size()>0 else True

    def top(self):
        return int(self.disks[self.get_size()-1].weight)

    def get_Stack(self):

        s = self.get_size() - 1
        while s >= 0:
            print("   ",self.disks[s])
            s = s - 1
            if s == -1 :
                print("----|----")
                print("##",self,"##\n")


    def add_disk(self,disk):
        self.disks.append(disk)

class Disk():

    def __init__(self,weight):

        self.weight = weight

    def __str__(self):
        return str(self.weight)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 honai.py <Number-of-disk-on-HonaiTower>")
    elif len(sys.argv) == 2:
        try :
            tower = HonaiTower(int(sys.argv[1]))
        except ValueError:
            print("Usage: python3 honai.py <Number-of-disk-on-HonaiTower>")
