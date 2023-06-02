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

def open_boxes():
    while True:
        for i in range(68):
            adbkit.tap(540, 520)
            time.sleep(0.5)
        adbkit.tap(1392, 305)
        time.sleep(0.5)
        adbkit.tap(1050, 700)
        time.sleep(1.5)
        adbkit.tap(800, 700)
        time.sleep(2)

class Stage:
    def __init__(self):
        self.handcards = select_card.Hand()        
        self.support_servant = ''
        self.support_craftessence = ''
        self.party_num = 3
        self.skill_list_1 = [[]]
        self.np_list_1 = []
        self.card_rule_1 = 'r'
        self.target_1 = 0
        self.skill_list_2 = [[]]
        self.np_list_2 = []
        self.card_rule_2 = 'r'
        self.target_2 = 0
        self.skill_list_3 = [[]]
        self.np_list_3 = []
        self.card_rule_3 = 'r'
        self.target_3 = 0
        self.apple = 'bronze'

        self.attack_img = cv2.imread('images/assets/attack.jpg')
        self.end_img = cv2.imread('images/assets/end.jpg')
        self.next_img = cv2.imread('images/assets/next.jpg')
        self.support_list_img = cv2.imread('images/assets/support.jpg')
        self.battle2_img = cv2.imread('images/assets/battle2.jpg')
        self.battle3_img = cv2.imread('images/assets/battle3.jpg')
    
    def run(self):
        support_mode = 0
        if self.support_servant != '':
            self.servant_img = cv2.imread(self.support_servant)
            support_mode += 1
        if self.support_craftessence != '':
            self.craftessence_img = cv2.imread(self.support_craftessence)
            support_mode += 2

        while True:
            print('Stage Start')            
            self.__battle(self.skill_list_1, self.np_list_1, self.card_rule_1, self.target_1, 1)
            print('Battle1 End')
            self.__battle(self.skill_list_2, self.np_list_2, self.card_rule_2, self.target_2, 2)
            print('Battle2 End')
            self.__battle(self.skill_list_3, self.np_list_3, self.card_rule_3, self.target_3, 3)
            print('Battle3 End')            
            self.__end_stage()
            print('Stage End')
            self.__next_stage(self.apple)
            print('Next Stage')
            self.__select_support(support_mode)
            print('Select Support')

    """
    def __select_stage(self):
        adbkit.tap(1000, 300) #enter first stage
        time.sleep(10)
        self.__select_support()
        time.sleep(1)
        adbkit.tap(self.party_num * 31 + 630, 63)
        time.sleep(1)
        adbkit.tap(1485, 850)
    """

    """
    def __select_class(self):
        match self.support_class:
            case 'caster':
                adbkit.tap(540, 160)
            case 'assassin':
                adbkit.tap(625, 160)
            case 'mix':
                adbkit.tap(880, 160)
            case _:
                print('unknown class')
                exit()
    """

    def __select_support(self, support_mode):
        # sup1 60 243 265 407
        # ce1 60 406 265 463
        # sup2 60 492 265 656
        # ce2 60 658 265 715
        #adbkit.tap(600, 350) # support_pos1
        #adbkit.tap(600, 600) # support_pos2
        #adbkit.tap(600, 800) # support_pos3
        while True:
            match support_mode:
                case 0:
                    adbkit.tap(600, 350)
                case 1:
                    if adbkit.check_exist(self.servant_img, 0, 0, 0, 0):
                        adbkit.tap(600, 350)
                    elif adbkit.check_exist(self.servant_img, 0, 0, 0, 0):
                        adbkit.tap(600, 600)
                case 2:
                    if adbkit.check_exist(self.craftessence_img, 55, 401, 215, 67):
                        adbkit.tap(600, 350)
                    elif adbkit.check_exist(self.craftessence_img, 55, 653, 215, 67):
                        adbkit.tap(600, 600)
                case 3:
                    if adbkit.check_exist(self.servant_img, 0, 0, 0, 0) and adbkit.check_exist(self.craftessence_img, 55, 401, 215, 67):
                        adbkit.tap(600, 350)
                    elif adbkit.check_exist(self.servant_img, 0, 0, 0, 0) and adbkit.check_exist(self.craftessence_img, 55, 653, 215, 67):
                        adbkit.tap(600, 600)
            time.sleep(3)
            if not adbkit.check_exist(self.support_list_img, 920, 115, 200, 90):
                break
            adbkit.tap(1065, 160) # refresh
            time.sleep(1)
            adbkit.tap(1050, 700) # refresh_ok
            time.sleep(10)

    def __battle(self, skill_list, np_list, card_rule, enemy_target, battle_num):
        adbkit.wait_until(self.attack_img, 1300, 700, 1550, 800)
        time.sleep(1)
        if enemy_target > 0:
            p = 3 - enemy_target
            adbkit.tap(200+300*p, 55)
        for skill_num, mate_target in skill_list:
            if skill_num > 10:
                self.__use_master_skill(skill_num, mate_target)
            else:
                self.__use_skill(skill_num, mate_target)
        while True:
            adbkit.tap(1475, 750)
            time.sleep(2)
            self.handcards.check_cardtype()
            self.handcards.detail()
            res = self.__attack(np_list, self.handcards.get_cardlist(card_rule), battle_num)
            if res != 'cont':
                break

    def __next_stage(self, apple):
        time.sleep(1)
        adbkit.tap(412, 768)
        time.sleep(0.5)
        adbkit.tap(1150, 700)
        time.sleep(0.5)
        #gold 400, silver 600 bronze 709
        if apple == 'gold':
            adbkit.tap(800, 400)
        elif apple == 'silver':
            adbkit.tap(800, 600)
        else:
            adbkit.tap(800, 709)
        time.sleep(0.5)
        adbkit.tap(1050, 700)
        time.sleep(8)

    def __end_stage(self):
        while True:
            adbkit.tap(800, 800)
            time.sleep(1)
            adbkit.tap(800, 800)
            time.sleep(1)
            if adbkit.check_exist(self.next_img, 1200, 750, 370, 110):
                adbkit.tap(1380, 850)
                time.sleep(1)
                adbkit.tap(1380, 850)
                time.sleep(1)
                adbkit.tap(1380, 850)
                break

    def __attack(self, np_list, card_list, battle_num):
        for np in np_list:
            adbkit.tap(np * 300 + 230, 250)
        for card in card_list:
            adbkit.tap(card * 320 - 160, 620)
        time.sleep(5)
        return self.__wait_result(battle_num)

    def __use_skill(self, skill_num, target):
        servant = (skill_num-1)//3+1
        skill = skill_num-servant*3+3
        adbkit.tap(servant * 397 + skill * 110 - 414, 725)
        if target > 0:
            time.sleep(1)
            adbkit.tap(target * 400 + 10, 540)
        time.sleep(4)

    def __use_master_skill(self, skill_num, mate_target):
        time.sleep(2)
        adbkit.tap(1495, 390)
        time.sleep(1)
        skill_num -= 10
        if skill_num > 10: #change
            src = skill_num - 10
            adbkit.tap(1356, 390)
            time.sleep(3)
            adbkit.tap(src * 250 - 75, 430)
            time.sleep(0.5)
            adbkit.tap(mate_target * 250 - 75, 430)
            time.sleep(0.5)
            adbkit.tap(800, 780)
            time.sleep(5)
        else:
            adbkit.tap(skill_num * 110 + 1026, 390)
            if mate_target > 0:
                time.sleep(1)
                adbkit.tap(mate_target * 400 + 10, 540)
        time.sleep(4)

    def __wait_result(self, battle_num):
        while True:
            screenshot = adbkit.screeshot()
            if adbkit.check_exist(self.attack_img, 1300, 700, 250, 100, screenshot=screenshot):
                time.sleep(1)
                match battle_num:
                    case 1:
                        if adbkit.check_exist(self.battle2_img, 1100, 10, 30, 40, screenshot=screenshot):
                            return 'next'
                        else:
                            return 'cont'
                    case 2:
                        if adbkit.check_exist(self.battle3_img, 1100, 10, 30, 40, screenshot=screenshot):
                            return 'next'
                        else:
                            return 'cont'
                    case 3:
                        return 'cont'
            if adbkit.check_exist(self.end_img, 80, 200, 310, 80, screenshot=screenshot):
                return 'end'