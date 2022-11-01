from abc import abstractmethod


class State:
    def __init__(self, player):
        self.player: AudioPlayer = player

    @abstractmethod
    def click_lock(self):
        ...

    @abstractmethod
    def click_play(self):
        ...

    @abstractmethod
    def click_next(self, is_double_click):
        ...

    @abstractmethod
    def click_previous(self, is_double_click):
        ...


class LockedState(State):
    def click_lock(self):
        if self.player.is_playing:
            self.player.change_state(PlayingState(self.player))
        else:
            self.player.change_state(ReadyState(self.player))

    def click_play(self):
        print('Did nothing')

    def click_next(self, _):
        print('Did nothing')

    def click_previous(self, _):
        print('Did nothing')


class ReadyState(State):
    def click_lock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        self.player.start_playback()
        self.player.change_state(PlayingState(self.player))

    def click_next(self, _):
        self.player.next_song()

    def click_previous(self, _):
        self.player.previous_song()


class PlayingState(State):
    def click_lock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        self.player.stop_playback()
        self.player.change_state(ReadyState(self.player))

    def click_next(self, is_double_click):
        if is_double_click:
            self.player.next_song()
        else:
            self.player.fast_forward()

    def click_previous(self, is_double_click):
        if is_double_click:
            self.player.previous_song()
        else:
            self.player.rewind()


class AudioPlayer:
    def __init__(self):
        self.state = ReadyState(self)
        self.playlist = ['Barbie Girl', 'Búp Bê Bằng Bông', 'Mysterious Girl']
        self.is_playing = False
        self.current_song = 0

    def click_lock(self):
        self.state.click_lock()

    def click_play(self):
        self.state.click_play()

    def click_next(self, is_double_click):
        self.state.click_next(is_double_click)

    def click_previous(self, is_double_click):
        self.state.click_previous(is_double_click)

    def start_playback(self):
        print(f'Started playback... [{self.playlist[self.current_song]}]')

    def stop_playback(self):
        print('Stopped playback')

    def next_song(self):
        if self.current_song == len(self.playlist) - 1:
            self.current_song = 0
        else:
            self.current_song += 1

        print(f'Next song... [{self.playlist[self.current_song]}]')

    def previous_song(self):
        if self.current_song == 0:
            self.current_song = len(self.playlist) - 1
        else:
            self.current_song -= 1

        print(f'Previous song... [{self.playlist[self.current_song]}]')

    def fast_forward(self):
        print('Skipped ahead 5 seconds')

    def rewind(self):
        print('Jumped back 5 seconds')

    def change_state(self, state):
        self.state = state
        print(f'Current state updated to: {state.__class__.__name__}')


def main():
    player = AudioPlayer()
    commands = ['lock', 'play', 'next', 'double_next', 'previous', 'double_previous']

    print(f"Available buttons: {', '.join(commands)}")
    while True:
        input_ = input('\nButton: ')
        if input_ == 'lock':
            player.click_lock()
        elif input_ == 'play':
            player.click_play()
        elif input_ == 'next':
            player.click_next(False)
        elif input_ == 'double_next':
            player.click_next(True)
        elif input_ == 'previous':
            player.click_previous(False)
        elif input_ == 'double_previous':
            player.click_previous(True)
        else:
            print('???')


if __name__ == '__main__':
    main()
