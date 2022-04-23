class Television:
    """
    An object representing television that provides methods to control the power, channel, and volume.
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Initialize the TV object with default values.
        """
        self.channel_num = 0
        self.volume_num = 0
        self.status = False


    def power(self):
        """
        Turns the TV on or off.
        """
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def channel_up(self):
        """
        Changes the channel to the next channel.
        """
        if self.status == True:
            if self.channel_num == self.MAX_CHANNEL:
                self.channel_num = self.MIN_CHANNEL
            else:
                self.channel_num += 1

    def channel_down(self):
        """
        Changes the channel to the previous channel.
        """
        if self.status == True:
            if self.channel_num == self.MIN_CHANNEL:
                self.channel_num = self.MAX_CHANNEL
            else:
                self.channel_num -= 1

    def volume_up(self):
        """
        Changes the volume to the next volume.
        """
        if self.status == True:
            if self.volume_num == self.MAX_VOLUME:
                pass
            else:
                self.volume_num += 1

    def volume_down(self):
        """
        Changes the volume to the previous volume.
        """
        if self.status == True:
            if self.volume_num == self.MIN_VOLUME:
                pass
            else:
                self.volume_num -= 1

    def __str__(self):
        """
        Returns a string representing the current status of the tv object.
        """
        return "TV status: Is on = {}, Channel = {}, Volume = {}".format(self.status, self.channel_num, self.volume_num)
