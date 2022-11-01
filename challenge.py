"""
Try to refactor this code to use the State Pattern
"""
class TeslaCar:
    def __init__(self):
        self.is_on = False
        self.is_moving = False

    def click_on(self):
        if self.is_on:
            self.off()
        else:
            self.on()

    def click_go(self, is_fast):
        if not self.is_on:
            print('Did nothing')
            return
        
        if self.is_moving:
            if is_fast:
                self.go_fast()
            else:
                self.go()
        else:
            self.go()

    def click_stop(self):
        if self.is_moving:
            self.stop()
        else:
            print('Did nothing')
    
    def on(self):
        self.is_on = True
        print('Engine On!')
    
    def off(self):
        self.is_on = False
        print('Engine Off!')

    def go(self):
        self.is_moving = True
        print(f'Moving!')
    
    def go_fast(self):
        print(f'Moving FASTER!')

    def stop(self):
        self.is_moving = False
        print('Stopped')


def main():
    car = TeslaCar()
    commands = ['on', 'go', 'go_fast', 'stop']

    print(f"Available buttons: {', '.join(commands)}")
    while True:
        input_ = input('\nButton: ')
        if input_ == 'on':
            car.click_on()
        elif input_ == 'go':
            car.click_go(False)
        elif input_ == 'go_fast':
            car.click_go(True)
        elif input_ == 'stop':
            car.click_stop()
        else:
            print('???')


if __name__ == '__main__':
    main()
