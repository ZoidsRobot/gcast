# LU MAU BOKEP GAK ? 🤣

bokep = ""
bocil = ""
tiktok = ""

# 
absen = [
    "**Hadir bang** 😁",
    "**Hadir kak** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir dick** 🤣",
    "**Hadir kak maap telat** 🥺",
]

"""
JANGAN HAPUS DEV && GUA GBAN LU KONTOL
CREDITS @XTSEA
"""
memek = [
    "**Speed Ultra** `999,999`",
    "**Speed Slow** `592.802`",
    "**Speed Power** `819.782`",
    "**Speed Extreme** `979.848`",
]

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

# BAYAR 25K PC @xtsea
