# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (c) 2025 Guillermo Leira Temes

import time
from . import client

# a cookie system made up in tinrux

class TinruxCookies:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = client.TinruxClient(host, port)
    def create_cookie(self, cookie_name, cookie_value, expire_time=None):
        """
        Create a new cookie.
        """
        if expire_time:
            self.client.send_command("SET", cookie_name, cookie_value)
            self.client.send_command("EXPIRE", cookie_name, expire_time)
        else:
            self.client.send_command("SET", cookie_name, cookie_value)
        return True
    def get_cookie(self, cookie_name):
        """
        Get a cookie by name.
        """
        cookie = self.client.send_command("GET", cookie_name)
        if cookie is None:
            return None
        elif cookie.startswith("ERR"):
            return None
        return cookie
    