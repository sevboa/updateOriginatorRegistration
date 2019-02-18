import sys
import time

class Counter:
    def __init__(self, count, delay):
        self.Count = count
        self.Form = '%' + str(len(list(str(count))) + 2) + 's/'
        self.Num = int()
        self.LastTellTime = float()
        self.Now = float()
        self.Delay = float(delay)
        self.CountStepDelay = int()
        self.AllSpeed = list()
        self.AverageSpeed = float()
    
    def tell(self, text):
        string = self.Form % self.Num + str(self.Count) + ' ' + text + ' (' + self.averageSpeed() + ') [' + self.timeLeft() + ']                    '
        sys.stdout.write(string)
        sys.stdout.flush()
        sys.stdout.write('\b' * len(string))
        #print(self.Num + '/' + str(self.Count) + ' ' + text, end="")
        
    def step(self, text):
        self.Num += 1
        self.Now = time.time()
        if self.Now - self.LastTellTime < self.Delay:
            self.CountStepDelay += 1
        else:
            self.tell(text)
            self.LastTellTime = time.time()
            self.CountStepDelay = 0
            
    def lastTell(self, text):
        #self.LastTellTime = float()
        self.tell(text)
        print()

    def averageSpeed(self):
        if self.CountStepDelay > 0:
            try:
                value = float(self.CountStepDelay) / (self.Now - self.LastTellTime)
            except ZeroDivisionError:
                value = 666.0
            self.AllSpeed.append(value)
            self.AverageSpeed = sum(self.AllSpeed) / len(self.AllSpeed)
        
        return str(round(self.AverageSpeed, 1)) + '/sec'
    
    def timeLeft(self):
        count = self.Count - self.Num
        if count != 0 and self.AverageSpeed != 0:
            return time.strftime('%X', time.gmtime(count / self.AverageSpeed))
        elif count == 0 and self.AverageSpeed != 0:
            return time.strftime('%X', time.gmtime(self.Count / self.AverageSpeed))
        else:
            return '0'


## Тестирование (при импорте не отрабатывает)
if __name__ == "__main__":
    a = [1,2,3]
    counter = Counter(len(a), 0.5)
    b = time.time()
    counter.step('Hello')
    time.sleep(0.9)
    counter.step('Hello')
    time.sleep(2)
    counter.step('Hello')
    time.sleep(2)
    counter.lastTell('Bye')
    print(time.time() - b)