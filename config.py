import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "20695198")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", "20695198"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "e8adeee627710bac3db1bd23e7dbdb1c")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBRX_t4wgfq_UbKmUu6HeVC_c11mhKtbIOWlZkCSYE3eEVWUKdJBS766ZD06TV0WeAhwfWjysmtYnFKV1lqAwlRZ1aHQl0C6tqAn4qk39BlMDQLn-3B9ha3tGYbE_3SfhHWj5810HnETgxCEOEc9viPsMPy68LjU09DxiOc5R84KJux02wj7BPWAYHIulJ4kiDvtMLx2gjUuenuE5oZdD0S8SvM-ns6deS0cmIzySSOFEQG_ar_Wi6k3aAHwau8cTGplY6-KwMgqtvbZqD7TQP2xLZN35SQ6x-AKBUEDwbIkaelskrEZgdR2-jvltQDhHGuIdAcreVhoZQIxr2LoRGaAAAAAWEepiMA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
