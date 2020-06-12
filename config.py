# set the following variable to True to declare that you have modified the config
i_have_read_config = False

# replace with the private token of your bot, do not share this with anyone
bot_token = "###########################################################"

# minimum amount of seconds between check
# e.g. compare amount of messages sent in channel within past 30 seconds
check_frequency = 30

# determine amount of messages per check_frequency required for each slowmode band
# slowmode_delay must be an integer ranging from 0-21600 seconds
time_configs = {
    # message_frequency: slowmode_delay
    0: 0,
    30: 1,
    60: 3,
    90: 5,
    120: 10
}

# choose whether channels must be whitelisted for auto-slowmode to run there
channel_whitelisting_enabled = True

# ids of channels that auto slowmode will run in
# ignored if channel whitelisting is disabled
whitelisted_channels = [
    00000000000000000,
    00000000000000000
]

# blacklisted channels ids
# if whitelisting is disabled, the bot will ignore channels with these ids
blacklisted_channels = [
    00000000000000000,
    00000000000000000
]
