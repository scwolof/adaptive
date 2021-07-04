from adaptive.client.client import Client

from adaptive.interface.user_data.constants import UserAccountCreation
from adaptive.interface.adaptive.constants import (
    UserAdRequest,
    UserAdResponse,
)
from adaptive.simul.users import User


class UserClient(Client):
    def __init__(self, user: User):
        super(UserClient).__init__()
        self.user = user

    def get_system_information(self):
        return None

    @Client.transmission
    def _create_account(self, userData) -> int:
        return self.client.createUserAccount(userData)

    def create_account(self) -> bool:
        # Create user account
        userData = UserAccountCreation(
            name=self.user.name,
            age=self.user.age_public,
            gender=self.user.gender_public,
        )
        success, self.user.uid = self._create_account(userData)
        return success

    @Client.transmission
    def _request_ads(self, reqData: UserAdRequest) -> UserAdResponse:
        return self.client.user_request(reqData)

    def request_ads(self) -> bool:
        reqData = UserAdRequest(
            uid=self.user.uid,
            sysinfo=self.get_system_information(),
        )
        # send ad request
        success, ad_response = self._request_ads(reqData)
        # Use ad_response
        print(ad_response)
        return success
