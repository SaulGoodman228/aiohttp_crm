import uuid

from aiohttp.web_response import json_response

from apps.crm.models import User
from apps.web.app import View


class AddUserView(View):
     async def post(self):
          data = await self.request.json()
          user = User(email=data['email'], _id=uuid.uuid4())
          return json_response(data={'status':'ok'})
