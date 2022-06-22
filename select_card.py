import cv2
import adbkit

#card_cy 650 760
#card_cx1 110 280
#card_cx2 430 600
#card_cx3 750 920
#card_cx4 1070 1240
#card_cx5 1395 1565

# card_w1 215 450 300 510
# card_w2 535 450 620 510
# card_w3 855 450 940 510
# card_w4 1175 450 1260 510
# card_w5 1500 450 1585 510

# card_r1 215  300 510
# card_r2 535 450 620 510
# card_r3 855 450 940 510
# card_r4 1175 450 1260 510
# card_r5 1500 450 1585 510

r = cv2.imread('images/assets/r.jpg')
g = cv2.imread('images/assets/g.jpg')
b = cv2.imread('images/assets/b.jpg')
weak = cv2.imread('images/assets/weak.jpg')
resist = cv2.imread('images/assets/resist.jpg')

class Hand:
    def __init__(self):
        self.clear()

    def clear(self):
        self.r = []
        self.g = []
        self.b = []
        self.rw = []
        self.gw = []
        self.bw = []
        self.rr = []
        self.gr = []
        self.br = []

    def check_cardtype(self):
        self.screenshot = adbkit.screeshot()

        self.clear()

        for index in range(1, 6):
            type = self.check_color(index)

            if (self.check_weak(index)):
                type = type + 'w'
            elif (self.check_resist(index)):
                type = type + 'r'

            match type:
                case 'r':
                    self.r.append(index)
                case 'g':
                    self.g.append(index)
                case 'b':
                    self.b.append(index)
                case 'rw':
                    self.rw.append(index)
                case 'gw':
                    self.gw.append(index)
                case 'bw':
                    self.bw.append(index)
                case 'rr':
                    self.rr.append(index)
                case 'gr':
                    self.gr.append(index)
                case 'br':
                    self.br.append(index)

                case _:
                    print('error')
                    exit()

    def get_cardlist(self, mode=''):
        match mode:
            case 'b':
                if len(self.bw + self.b + self.br) > 2:
                    return self.bw + self.b + self.br
                else:
                    return self.bw + self.b + self.br + self.rw + self.gw + self.r + self.g + self.rr + self.gr
            case 'w':
                return  self.rw + self.bw + self.gw + self.r + self.b + self.g + self.rr + self.br + self.gr
            case _:
                if len(self.bw + self.b + self.br) > 2:
                    return self.bw + self.b + self.br
                else:
                    return self.rw + self.bw + self.gw + self.r + self.b + self.g + self.rr + self.br + self.gr

    def detail(self):
        print('r:', self.rw + self.r + self.rr)
        print('g:', self.gw + self.g + self.gr)
        print('b:', self.bw + self.b + self.br)
        print('weak:', self.rw + self.bw + self.gw)
    
    def check_color(self, index):
        if index == 5:
            x = 1395
        else:
            x = index * 320 - 210
        if adbkit.check_exist(r, x, 650, 170, 110, screenshot=self.screenshot):
            return 'r'
        elif adbkit.check_exist(g, x, 650, 170, 110, screenshot=self.screenshot):
            return 'g'
        else:
            return 'b'

    def check_weak(self, index):
        if index == 5:
            x = 1500
        else:
            x = index * 320 - 105
        if adbkit.check_exist(weak, x, 380, 85, 160, screenshot=self.screenshot):
            return True
        else:
            return False

    def check_resist(self, index):
        if index == 5:
            x = 1500
        else:
            x = index * 320 - 105
        if adbkit.check_exist(resist, x, 360, 85, 160, screenshot=self.screenshot):
            return True
        else:
            return False