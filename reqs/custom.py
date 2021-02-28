import utils
import json
import traceback
from bili_global import API_LIVE


class BuyLatiaoReq:
    # 其实与utils部分差不多，怀疑可能是新旧api
    @staticmethod
    async def fetch_livebili_userinfo_pc(user):
        url = f'{API_LIVE}/xlive/web-ucenter/user/get_user_info'
        json_rsp = await user.bililive_session.request_json('GET', url, headers=user.pc.headers)
        return json_rsp


class BuyMedalReq:
    @staticmethod
    async def buy_medal(user, uid, coin_type):
        url = f'https://api.vc.bilibili.com/link_group/v1/member/buy_medal'
        data = {
            'coin_type': coin_type,
            'master_uid': uid,
            'platform': 'android',
            'csrf_token': user.dict_user['csrf'],
            'csrf': user.dict_user['csrf']
        }
        json_rsp = await user.other_session.request_json('POST', url, data=data, headers=user.pc.headers)
        return json_rsp


class BanUserReq:
    @staticmethod
    async def ban_user(user, room_id: int, uid: int, hour: int):
        url = f'{API_LIVE}/banned_service/v2/Silent/add_block_user'
        data = {
            'roomid': room_id,
            'block_uid': uid,
            'hour': hour,
            'csrf_token': user.dict_user['csrf'],
            'csrf': user.dict_user['csrf'],
        }
        json_rsp = await user.other_session.request_json('POST', url, data=data, headers=user.pc.headers)
        return json_rsp



class TopUserReq:
    @staticmethod
    async def top_user(user, room_id: int, uid: int, page: int = 1):
        url = f'{API_LIVE}/xlive/app-room/v2/guardTab/topList?roomid={room_id}&page={page}&ruid={uid}&page_size=29'
        json_rsp = await user.other_session.request_json('GET', url, headers=user.pc.headers)
        return json_rsp

class QQReq:
    @staticmethod
    async def auth(user, host: str, auth_key: str):
        url = f'http://{host}/auth'
        data = {
            'authKey': auth_key
        }
        # json_rsp = await user.other_session.orig_req_json('POST', url, data=data)
        # return json_rsp
        # print(url, data)
        async with user.other_session.session.request('POST', url, data=json.dumps(data)) as rsp:
            body = await rsp.json()
            return body

    @staticmethod
    async def verify(user, host, qq: int, session: str):
        
        url = f'http://{host}/verify'
        data = {
            'sessionKey': session,
            'qq': qq,
        }
        # print(url, data)
        async with user.other_session.session.request('POST', url, data=json.dumps(data)) as rsp:
            body = await rsp.json()
            return body
        # json_rsp = await user.other_session.orig_req_json('POST', url, data=data)
        # return json_rsp

    @staticmethod
    async def sendGroupMessage(user, host, session: str, target: int, messageChain: list = []):
        url = f'http://{host}/sendGroupMessage'
        data = {
            'sessionKey': session,
            'target': int(target),
            'messageChain': messageChain,
        }
        # print(url, data)
        async with user.other_session.session.request('POST', url, data=json.dumps(data)) as rsp:
            body = await rsp.json()
            return body
        # json_rsp = await user.other_session.orig_req_json('POST', url, data=data)
        # return json_rsp
    