# discord-auto-slowmode by JoshSCF (joshl.io)

import config, discord, time
client = discord.Client()

message_cache = {}
previous_delays = {}
last_updated = 0


def get_delay(message_count):
    # get message limits in descending order, compare with message count
    message_limits = sorted(config.time_configs.keys(), reverse=True)

    for limit in message_limits:
        if message_count >= limit:
            # return delay determined in config
            return config.time_configs[limit]
    
    # if nothing already returned, return a slowmode delay of 0
    return 0


async def update_slowmode():
    global last_updated, message_cache, previous_delays
    new_channel_delays = {}

    # iterate through cache and fetch new delay times
    for channel_id in message_cache.keys():
        delay = get_delay(message_cache[channel_id])

        # if delay is the same as previous delay, skip iteration
        if channel_id in previous_delays.keys():
            if previous_delays[channel_id] == delay:
                new_channel_delays[channel_id] = delay
                continue
        
        # edit channel slowmode and update new_channel_delays
        channel = client.get_channel(channel_id)
        await channel.edit(slowmode_delay=delay)
        new_channel_delays[channel_id] = delay

    
    # reset message cache and update last_updated & previous_delays
    message_cache = {}
    last_updated = time.time()
    previous_delays = new_channel_delays


@client.event
async def on_message(message):
    global last_updated, message_cache
    channel_id = message.channel.id

    # update slowmode if it has been x seconds since last update
    if time.time() >= last_updated + config.check_frequency:
        await update_slowmode()
    
    # ignore message if channel blacklisted or not whitelisted
    if config.channel_whitelisting_enabled:
        if channel_id not in config.whitelisted_channels:
            return
    else:
        if channel_id in config.blacklisted_channels:
            return

    # add channel id to cache if not already added
    if message.channel.id not in message_cache.keys():
        message_cache[channel_id] = 1
        return
    
    # increase message count by 1 for channel if cache exists
    message_cache[channel_id] += 1


if not config.i_have_read_config:
    # user has not read config file, don't start code
    print("You must modify config.py before running!")
    input("Press enter to continue...")
    exit()

client.run(config.bot_token)
