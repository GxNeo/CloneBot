from pyrogram import Client
from pyrogram.errors import PeerIdInvalid
from pyrogram.errors import UserNotParticipant
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import MessageMediaPhoto, MessageMediaVideo, MessageMediaDocument

# API credentials and session name
api_id = 123456 # Enter your API ID here
api_hash = 'abcdefghijklmnopqrstuvwxyz012345' # Enter your API hash here
session_name = 'my_bot_session' # Enter a name for your session

# Source and destination channel IDs
source_channel_id = -1001234567890 # Enter the ID of your source channel here
destination_channel_id = -1000987654321 # Enter the ID of your destination channel here

# Start and end message IDs
start_message_id = 1
end_message_id = 150

# Start the Pyrogram client
app = Client(session_name, api_id, api_hash)

# Function to forward media messages with captions from source to destination channel
async def forward_media_messages():
    try:
        # Get the source channel object
        source_channel = await app.get_chat(source_channel_id)

        # Get the destination channel object
        destination_channel = await app.get_chat(destination_channel_id)

        # Loop through the messages and forward media messages to destination channel
        for message_id in range(start_message_id, end_message_id+1):
            message = await app.get_messages(source_channel_id, message_id)
            if message.media:
                media_message = None
                if isinstance(message.media, MessageMediaPhoto):
                    media_message = await app.forward_messages(chat_id=destination_channel_id, from_chat_id=source_channel_id, message_ids=message.id, as_copy=True, caption=message.caption)
                elif isinstance(message.media, MessageMediaVideo):
                    media_message = await app.forward_messages(chat_id=destination_channel_id, from_chat_id=source_channel_id, message_ids=message.id, as_copy=True, caption=message.caption)
                elif isinstance(message.media, MessageMediaDocument):
                    media_message = await app.forward_messages(chat_id=destination_channel_id, from_chat_id=source_channel_id, message_ids=message.id, as_copy=True, caption=message.caption)

                if media_message is not None:
                    print(f'Forwarded message {message.id} to destination channel {destination_channel_id}')

                    # Wait for 10 seconds before forwarding the next message
                    await asyncio.sleep(10)

    except PeerIdInvalid:
        print('Invalid channel ID provided')
    except UserNotParticipant:
        print('You are not a member of the channel')
    except ChatAdminRequired:
        print('You must be an admin of the channel')



# Run the function to forward media messages
with app:
    app.loop.run_until_complete(forward_media_messages())
