import sys

from pyrogram import Client

import config

from ..logging import LOGGER



class VipXBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot..")
        super().__init__(
            "VipXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "𝐏𝐥𝐞𝐚𝐬𝐞 𝐩𝐫𝐨𝐦𝐨𝐭𝐞 𝐁𝐨𝐭 𝐚𝐬 𝐀𝐝𝐦𝐢𝐧 𝐢𝐧 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩"
            )
            sys.exit()
        LOGGER(__name__).info(f"AnshuxMusicBot Started as {self.name}")
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐛𝐚𝐛𝐲😉 **\n\n👀 𝐈𝐃 : `{self.id}`\n🥵𝐍𝐀𝐌𝐄 : {self.name}\n🖤 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : @{self.username}"
            )
        except:
            LOGGER(__name__).error(
                "𝐁𝐨𝐭 𝐡𝐚𝐬 𝐟𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐡𝐞 𝐥𝐨𝐠 𝐆𝐫𝐨𝐮𝐩. 𝐌𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐭𝐡𝐚𝐭 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐚𝐝𝐝𝐞𝐝 𝐲𝐨𝐮𝐫 𝐛𝐨𝐭 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐥𝐨𝐠 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐩𝐫𝐨𝐦𝐨𝐭𝐞𝐝 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧!"
            )
            sys.exit()
