from typing import List, Union
from pydantic import BaseModel

from py_ocpi.core.data_types import CiString, URL, String
from py_ocpi.core.enums import RoleEnum
from py_ocpi.modules.locations.v_2_2_1.schemas import BusinessDetails


class CredentialsRole(BaseModel):
    """
    https://github.com/ocpi/ocpi/blob/2.2.1/credentials.asciidoc#141-credentialsrole-class
    """
    role: RoleEnum
    business_details: BusinessDetails
    party_id: Union[CiString(3), None]
    country_code: Union[CiString(2), None]


class Credentials(BaseModel):
    """
    https://github.com/ocpi/ocpi/blob/2.2.1/credentials.asciidoc#131-credentials-object
    """
    token: String(64)
    url: URL
    roles: List[CredentialsRole]
