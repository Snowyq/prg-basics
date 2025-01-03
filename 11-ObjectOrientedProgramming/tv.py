class TV:
    channel_no = 1
    channels = []
    is_on = False
    volume = 0

    def __init__(self, producent, model, screen_size):
        self.producent = producent
        self.model = model
        self.screen_size = screen_size

    def increase_vol(self):
        if self.is_on:
            volume = volume + 1 if volume < 10 else volume

    def decrease_vol(self):
        if self.is_on:
            volume = volume - 1 if volume > 0 else volume

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, nr):
        self.channel_no = nr

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print("Channel list:")
        for i, name in enumerate(self.channels):
            print(f"{i + 1}. {name}")

    def show_status(self):
        num = self.channel_no
        if len(self.channels) > num:
            channel = self.channels[num]
        else:
            channel = ""
        print(
            "on" if self.is_on else "off",
            f"channel nr: {self.channel_no} {channel} volume: {self.volume}",
        )
