from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InputMediaPhoto, InputMediaVideo

# Replace with your own API credentials
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# Replace with the IDs of the source and destination channels
source_channel_id = -1001234567890
dest_channel_id = -1009876543210

# Define the range of message IDs to copy
start_id = 1
end_id = 200

# Create the Pyrogram client
client = Client('my_bot', api_id, api_hash, bot_token=bot_token)

@client.on_message(filters.channel(source_channel_id) & (filters.photo | filters.video) & filters.inverted(filters.edited))
async def copy_media(client, message):
    try:
        # Copy the media to the destination channel
        if message.photo:
            media = InputMediaPhoto(message.photo.file_id, caption=message.caption)
        elif message.video:
            media = InputMediaVideo(message.video.file_id, caption=message.caption)

        await client.send_media_group(dest_channel_id, media)

    except FloodWait as e:
        # Wait if we hit a rate limit
        print(f'FloodWait for {e.x} seconds.')
        await asyncio.sleep(e.x)

    except Exception as e:
        print(f'Error copying message {message.message_id}: {e}')

async def main():
    # Start the client
    await client.start()

    # Copy the messages from the source channel to the destination channel
    async for message in client.iter_history(source_channel_id, offset_id=start_id, reverse=True):
        if message.message_id > end_id:
            break

        # Skip the message if it's not a photo or video
        if not (message.photo or message.video):
            continue

        # Copy the message to the destination channel
        await copy_media(client, message)

        # Pause the script for 10 seconds
        await asyncio.sleep(10)

    # Stop the client
    await client.stop()

if __name__ == '__main__':
    # Run the script
    import asyncio
    asyncio.run(main())
