#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) @GetSongs
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import filters
from pyrogram.types import Message
from bot import (
    GROUP_CALLS,
    AUTH_USERS,
    COMMAND_HANDLER,
    STOP_COMMAND_HNTTH,
    START_ED_PROC_ING_MESG
)
from bot.bot import Bot


@Bot.on_message(
    filters.user(AUTH_USERS) &
    filters.command(STOP_COMMAND_HNTTH, COMMAND_HANDLER)
)
async def stop_commnd_fn(_, message: Message):
    # send a message, use it to update the progress when required
    status_message = await message.reply_text(
        START_ED_PROC_ING_MESG,
        quote=True
    )

    try:
        _chat_id = message.command[1]
        if _chat_id.startswith("-100"):
            _chat_id = int(_chat_id)
        else:
            _chat_id = (await message._client.get_chat(_chat_id)).id
    except IndexError:
        _chat_id = message.chat.id

    if group_call := GROUP_CALLS.get(_chat_id):
        await group_call.stop()

    await status_message.delete()
