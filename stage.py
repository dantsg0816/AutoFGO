from tabnanny import check
from tkinter import Frame
import cv2
import time

from numpy import mat, ndarray
import adbkit
import select_card

# 關卡 1000 300

# caster 540 160
# mix 880 160    
# refresh 1065 160
# refresh_ok 1050 700
# sup1 60 243 265 407
# ce1 60 406 265 463
# sup2 60 492 265 656
# ce2 60 658 265 715

# party_i 630+31*i 63
# mission_start 1485 850

# attack 1320 710 1530 790
# master_skill 1495 390
# ms1 1136 390
# ms2 1246 390
# ms3 1356 390
# p1s1 93 725
# p1s2 203 725
# p1s3 313 725
# p2s1 490 725
# p2s2 600 725
# p2s3 710 725
# p3s1 887 725
# p3s2 997 725
# p3s3 1107 725
# select_p1 410 540
# select_p2 810 540
# select_p3 1210 540

# np1 530 250
# np2 830 250
# np3 1130 250

# card1_w 215 450 300 510
# card2_w 535 450 620 510
# card3_w 855 450 940 510
# card4_w 1175 450 1260 510
# card5_w 1500 450 1585 510

# change_p1 175 430
# change_p2 425 430
# change_p3 675 430
# change_p4 925 430
# change_p5 1175 430
# change_p6 1425 430
# change_ok 800 780

attack_img = cv2.imread('images/assets/attack.jpg')
end_img = cv2.imread('images/assets/end.jpg')

battle1 = cv2.imread('images/assets/battle1.jpg')
battle2 = cv2.imread('images/assets/battle2.jpg')
battle3 = cv2.imread('images/assets/battle3.jpg')

class Stage:
    def __init__(self):
        self.support_class = 'mix'
        self.servant = ''
        self.craftessence = ''
        self.party_num = 3

        self.hand = select_card.Hand()

    def __select_stage(self):
        adbkit.tap(1000, 300) #enter first stage
        time.sleep(4)
        self.__select_class()
        time.sleep(1)
        self.__select_support()
        time.sleep(1)
        adbkit.tap(self.party_num * 31 + 630, 63)
        time.sleep(1)
        adbkit.tap(1485, 850)

    def __select_class(self):
        match self.support_class:
            case 'caster':
                adbkit.tap(540, 160)
            case 'mix':
                adbkit.tap(880, 160)
            case _:
                print('unknown class')
                exit()

    def __select_support(self):
        # sup1 60 243 265 407
        # ce1 60 406 265 463
        # sup2 60 492 265 656
        # ce2 60 658 265 715
        print('select support')
        while True:
            #region 1
            if True:
                adbkit.tap(600, 350) # support_pos1
                break
            #region 2
            if adbkit.check_exist(self.servant, x, y, w, h) and adbkit.check_exist(self.craftessence, x, y, w, h):
                adbkit.tap(600, 600) # support_pos2
                break
            time.sleep(15)
            adbkit.tap(1065, 160) # refresh
            adbkit.tap(1050, 700) # refresh_ok

    def run(self):
        self.support_class = 'mix'
        self.servant = ''
        self.craftessence = ''
        self.party_num = 3

        #self.__select_stage()
        print('stage start')

        adbkit.wait_until(attack_img, 1300, 700, 1550, 800)
        #self.__use_skill(2, 3, 1)
        #self.__use_skill(3, 3, 1)
        #self.__use_skill(2, 2, 1)
        #self.__use_skill(3, 2, 1)
        #self.__use_skill(2, 1)
        #self.__use_skill(3, 1)
        while True:
            adbkit.tap(1475, 750)
            time.sleep(3)
            self.hand.check_cardtype()
            self.hand.detail()
            res = self.__attack([1, 2, 3], self.hand.get_cardlist(), 1)
            if res == 'next':
                print('next')
                break
            if res == 'end':
                print('end')
                break

    def __attack(self, np_list, card_list, battle_num):
        for np in np_list:
            adbkit.tap(np * 300 + 230, 250)
        for card in card_list:
            adbkit.tap(card * 320 - 160, 620)
        time.sleep(5)
        return self.__wait_result(battle_num)

    def __use_skill(self, servant_num, skill_num, target=0):
        adbkit.tap(servant_num * 397 + skill_num * 110 - 414, 725)
        time.sleep(1)
        if target > 0:
            adbkit.tap(target * 400 + 10, 540)
        adbkit.wait_until(attack_img, 1300, 700, 1550, 800)

    def __use_master_skill(self, skill_num, target=0):
        adbkit.tap(1495, 390)
        adbkit.tap(skill_num * 110 + 1026, 390)
        if target > 0:
            adbkit.tap(target * 400 + 10, 540)
        adbkit.wait_until(attack_img, 1300, 700, 1550, 800)

    def __use_master_change(self, src, dst):
        adbkit.tap(1495, 390)
        adbkit.tap(1356, 390)
        adbkit.tap(src * 250 - 75, 430)
        adbkit.tap(dst * 250 - 75, 430)
        adbkit.tap(800, 780)
        adbkit.wait_until(attack_img, 1300, 700, 1550, 800)

    def __wait_result(self, battle_num):
        while True:
            screenshot = adbkit.screeshot()
            if adbkit.check_exist(attack_img, 1300, 700, 250, 100, screenshot=screenshot):
                match battle_num:
                    case 1:
                        if adbkit.check_exist(battle2, 1075, 15, 30, 35, screenshot=screenshot):
                            return 'next'
                        else:
                            return 'cont'
                    case 2:
                        if adbkit.check_exist(battle3, 1075, 15, 30, 35, screenshot=screenshot):
                            return 'next'
                        else:
                            return 'cont'
            if adbkit.check_exist(end_img, 80, 200, 310, 80, screenshot=screenshot):
                return 'end'