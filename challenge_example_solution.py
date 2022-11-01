class State:
    def __init__(self, car):
        self.car = car

    def click_on(self):
        ...

    def click_go(self, is_fast):
        ...

    def click_stop(self):
        ...


class OffState(State):
    def click_on(self):
        self.car.on()
        self.car.change_state(OnState(self.car))

    def click_go(self, _):
        print('Did nothing')

    def click_stop(self):
        print('Did nothing')


class MovingState(State):
    def click_on(self):
        print('Did nothing')

    def click_go(self, is_fast):
        if is_fast:
            self.car.go_fast()
        else:
            self.car.go()

    def click_stop(self):
        self.car.stop()
        self.car.change_state(OnState(self.car))


class OnState(State):
    def click_on(self):
        self.car.off()
        self.car.change_state(OffState(self.car))

    def click_go(self, _):
        self.car.go()
        self.car.change_state(MovingState(self.car))

    def click_stop(self):
        print('Did nothing')


class TeslaCar:
    def __init__(self):
        self.state = OffState(self)
    
    def change_state(self, state):
        self.state = state
        print(f'Changed state [{self.state.__class__.__name__}]')

    def click_on(self):
        self.state.click_on()

    def click_go(self, is_fast):
        self.state.click_go(is_fast)

    def click_stop(self):
        self.state.click_stop()
    
    def on(self):
        print('Engine On!')
    
    def off(self):
        print('Engine Off!')

    def go(self):
        print(f'Moving!')
    
    def go_fast(self):
        print(f'Moving FASTER!')

    def stop(self):
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
