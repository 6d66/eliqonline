#!/usr/bin/env python
#
#  A library for Eliq Online API
#  Copyright (C) 2015 Magnus F <magnus@fet.nu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

import urllib
import json

from .datanow import DataNow
from .data import Data
from datetime import datetime


class API():
    """ API class for Eliq Online API  """

    # Base url to Eliq Online API
    BASE_URL = "https://my.eliq.se/api"

    # Access token for API
    ACCESS_TOKEN = None

    def __init__(self, access_token):
        self.ACCESS_TOKEN = access_token

    def get_data_from_eliq(self, function, parameters=None):
        if parameters is None:
            parameters = ""

        api_url = "%s/%s?accesstoken=%s%s" % (
            self.BASE_URL,
            function,
            self.ACCESS_TOKEN,
            parameters
        )

        api_open = urllib.urlopen(api_url)
        api_code = api_open.getcode()
        api_content = api_open.read()
        api_content = api_content.decode('utf-8')

        if api_code == 400:
            print api_content
            return None
        else:
            return api_content

    def get_data(self, startdate, intervaltype, enddate, channelid):
        data = Data()
        return data

    def get_data_now(self, channelid=None):
        function = "datanow"
        parameters = None

        if channelid is not None:
            parameters = "&channelid=%d" % (channelid)

        eliqData = self.get_data_from_eliq(function, parameters)

        if eliqData is None:
            return None
        else:
            jsonData = json.loads(eliqData)
            eliq_data_now = DataNow()
            eliq_data_now.power = float(jsonData["power"])
            eliq_data_now.channelid = jsonData["channelid"]
            eliq_data_now.createddate = datetime.strptime(
                jsonData["createddate"],
                "%Y-%m-%dT%H:%M:%S"
            )
            return eliq_data_now
