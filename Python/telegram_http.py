from ..instance.config import TELEGRAM_TOKEN
import httpx

async def sendTgMessage(cls,chatid:str,message: str):
    tg_msg = {"chat_id": chatid, "text": message, "parse_mode": "Markdown"}
    API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    async with httpx.AsyncClient() as client:
        await client.post(API_URL, json=tg_msg)


async def create_user(cls, user:UserRegisterForm):
    userdata = await cls.get_user_by_email(user.email)
    if userdata:
        return False
    else:
        data = {'userid':user.username, 'email':user.email, 'chatid':user.chatid,'spaces':{}, 'hashed_password':get_password_hash(user.password)}
        ee = f"Register email : {user.email}"
        await sendTgMessage(user.chatid,ee)
        return True