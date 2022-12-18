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

ANAK_BANGSAD = [
    "https://telegra.ph/file/34229dab464365da8be02.jpg"
    "https://telegra.ph/file/e7535adc7b835f6c6efa4.jpg"
    "https://telegra.ph/file/a19d05e1da734a506d76d.jpg"
    "https://telegra.ph/file/69e585b4c123a3aa82e45.jpg"
    "https://telegra.ph/file/872dbe33a146dce3f843e.jpg"

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
