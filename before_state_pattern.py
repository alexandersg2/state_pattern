from abc import abstractmethod


class AudioPlayer:
    def __init__(self):
        self.playlist = ['Barbie Girl', 'Búp Bê Bằng Bông', 'Mysterious Girl']
        self.is_playing = False
        self.current_song = 0
        self.is_locked = False

    def click_lock(self):
        if self.is_locked:
            self.unlock()
        else:
            self.lock()

    def click_play(self):
        if self.is_locked:
            print('Did nothing')
            return
        
        if self.is_playing:
            self.stop_playback()
        else:
            self.start_playback()

    def click_next(self, is_double_click):
        if self.is_locked:
            print('Did nothing')
            return
        
        if not self.is_playing:
            self.next_song()
        else:
            if is_double_click:
                self.next_song()
            else:
                self.fast_forward()

    def click_previous(self, is_double_click):
        if self.is_locked:
            print('Did nothing')
            return
        
        if not self.is_playing:
            self.previous_song()
        else:
            if is_double_click:
                self.previous_song()
            else:
                self.rewind()
    
    def lock(self):
        self.is_locked = True
        print('Locked!')
    
    def unlock(self):
        self.is_locked = False
        print('Unlocked!')

    def start_playback(self):
        self.is_playing = True
        print(f'Started playback... [{self.playlist[self.current_song]}]')

    def stop_playback(self):
        self.is_playing = False
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
