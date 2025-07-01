'''
    0, 0 에서 시작
    격자 상하좌우 최대 사이즈 5
'''

def solution(dirs):
    class game:
        def __init__(self):
            self.rule = {
                'U': [0, 1],
                'D': [0, -1],
                'R': [1, 0],
                'L': [-1, 0]
            }
            self.now_x = 0
            self.now_y = 0
            self.check = []
            self.cnt = 0

        def run(self, go):
            tmp_x = self.now_x + self.rule[go][0]
            tmp_y = self.now_y + self.rule[go][1]
            
            if -5 > tmp_x or 5 < tmp_x or -5 > tmp_y or 5 < tmp_y:
                return

            if [self.now_x, self.now_y, tmp_x, tmp_y] not in self.check:
                self.check.append([self.now_x, self.now_y, tmp_x, tmp_y])
                self.check.append([tmp_x, tmp_y, self.now_x, self.now_y])
                self.cnt += 1
                
            self.now_x = tmp_x
            self.now_y = tmp_y
    
    game = game()
    for dir in dirs:
        game.run(dir)
    
    answer = game.cnt
    return answer