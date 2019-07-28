import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.contact.startswith("/타오봇 안녕"):
        await message.channel.send("랄루랄루랄~! 그래 안녕")

    if message.contact.startswith("/타오봇 뭐해"):
        await message.contact.send("나 지금 Minecraft 플레이 중이야")

    if message.contact.startswith("/타오봇 심심해"):
        await message.contact.send("유튜브 봐")

    if message.contact.startswith("/타오봇 밥뭐먹을까"):
        await message.contact.send("[아침: 식빵, 점심: 라면, 저녁: 치킨]을(를) 추천합니다.")

    if message.contact.startswith("/타오봇 이벤트"):
        await message.contact.send("현재 이벤트는 [타오가 구독해주는 이벤트] 가 있습니다.")

    if message.contact.startswith("/타오봇 설명"):
        await message.contact.send("안녕하세요! 저는 타오봇이라고 합니다! 여러 명령어들을 입력하시면 제가 답변해드립니다!")

    if message.contact.startswith("/타오봇 명령어"):
        await message.contact.send("/타오봇 [안녕,뭐해,심심해,밥뭐먹을까,이벤트,설명,명령어]")
        

access_token = os environ["BOT_TOKEN"]
client.run(access_token)
