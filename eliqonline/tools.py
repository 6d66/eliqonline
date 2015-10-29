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

try:
    import urllib.request as urllib
except ImportError:
    import urllib2 as urllib

from datetime import datetime


class Tools(object):
    """ Tool class for Eliq Online API  """

    # Base url to Eliq Online API
    BASE_URL = "https://my.eliq.se/api"

    # Access token for API
    ACCESS_TOKEN = None

    # Date format, (ISO 8601, European)
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

    def __init__(self, access_token=None):
        if access_token is not None:
            self.ACCESS_TOKEN = access_token

    def get_data_from_eliq(self, function, parameters=None):
        if parameters is None:
            parameters = ""

        # Build API request url
        api_url = "%s/%s?accesstoken=%s%s" % (
            self.BASE_URL,
            function,
            self.ACCESS_TOKEN,
            parameters.replace(" ", "%20")
        )

        api_open = urllib.urlopen(api_url)

        try:
            api_content = api_open.read()
            return api_content
        except urllib.HTTPError as e:
            if e.code == 400:
                print(api_content)
            return None

    def maybe_to_date(self, date_string):
        if date_string is not None:
            return self.to_date(date_string)
        else:
            return None

    def to_date(self, date_string):
        return datetime.strptime(
            date_string,
            self.DATE_FORMAT
        )

    def maybe_to_float(self, float_string):
        if float_string is not None:
            return float(float_string)
        else:
            return None
