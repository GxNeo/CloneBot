from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, PeerIdInvalid
from pyrogram import types
import asyncio
from config import Config 
from bot import User as app


HELLO = """
api_id = Config.API_ID
api_hash = Config.API_HASH
session_name = Config.TG_USER_SESSION
"""
# Source and destination channel IDs
source_channel_id = -1001810218788 # Enter the ID of your source channel here
destination_channel_id = -1001427229068 # Enter the ID of your destination channel here

# Start and end message IDs
start_message_id = 3
end_message_id = 189617

HELLOR = """
# Start the Pyrogram client
app = Client(session_name, api_id, api_hash)
"""


# Function to forward media messages from source to destination channel
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
                if isinstance(message.media, types.Photo):
                    media_message = await app.forward_messages(chat_id=destination_channel_id, from_chat_id=source_channel_id, message_ids=message.message_id, as_copy=True)
                elif isinstance(message.media, types.Video):
                    media_message = await app.forward_messages(chat_id=destination_channel_id, from_chat_id=source_channel_id, message_ids=message.message_id, as_copy=True)
                elif isinstance(message.media, types.Document):
                    media_message = await app.forward_messages(chat_id=destination_channel_id, from_chat_id=source_channel_id, message_ids=message.message_id, as_copy=True)

                if media_message is not None:
                    print(f'Forwarded message {message.message_id} to destination channel {destination_channel_id}')

                    # Add a delay of 10 seconds before forwarding the next message
                    await asyncio.sleep(10)

    except PeerIdInvalid:
        print('Invalid channel ID provided')
    except UserNotParticipant:
        print('You are not a member of the channel')
    except ChatAdminRequired:
        print('You must be an admin of the channel')


# Define the start command
@app.on_message(filters.command('start'))
async def start_command_handler(client, message):
    await message.reply('Hi, I am ready to forward media messages!')


# Define the command to start forwarding media messages
@app.on_message(filters.command('forward'))
async def forward_command_handler(client, message):
    await message.reply('Started forwarding media messages!')
    await forward_media_messages()


HELLOT = """
# Run the client
print("User Started 🔥")
app.run()
"""
