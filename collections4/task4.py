stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98, 'Тестовый канал' : 159}

channel_name = ''
channel_effort = 0

for channel in stats.keys():
    if stats.get(channel) > channel_effort:
        channel_name = channel
        channel_effort = stats.get(channel)

print(f'Лучший канал продаж: {channel_name}  {channel_effort} продаж')