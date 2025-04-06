#    Tinrux Cli a database writed on python
#    Copyright (C) 2025  Guillermo Leira Temes
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from . import tinruxClient as client
from . import tinruxServer as server

message = """    Tinrux  Copyright (C) 2025  Guillermo Leira Temes
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions."""

help_msg = " usage : tinrux [server/client] [host] [port] [new] \n (new when it's a new server) \n other options: \n \t help → tinrux help"
def main():
	try:
		if sys.argv[1]=="help":
			print(help_msg)
		#other logic
		elif sys.argv[1]=="server":
			host = sys.argv[2]
			port = sys.argv[3]
			try:
				new = sys.argv[4]
				if new == "new":
					cliServer = server.TinruxServer(host, int(port))
				else:
					cliServer = server.TinruxServer(host, int(port), new=False)
			except Exception:
				cliServer = server.TinruxServer(host, int(port), new=False)
			print(message)
			cliServer.main()
		elif sys.argv[1]=="client":
			host = sys.argv[2]
			port = sys.argv[3]
			cliClient = client.TinruxClient(host, int(port))
			print(message)
			print("Type 'exit' or 'quit' to exit.")
			command = input(f"({host}:{port})>>> ")
			while True:
				if command == "exit" or command == "quit":
					break
				opt = command.split()[0]
				args = command.split()[1:]
				response = cliClient.send_command(opt, *args)
				print(response)
				command = input(f"({host}:{port})>>> ")
			print("Exiting...")
			cliClient.close()
		else:
			print("Unknown option, type 'tinrux help' for help")
	except Exception:
		print("Bad Usage, type 'tinrux help' for help")