# NetExec version of the CME module.
# Author  : TRIKKSS
# discord : TRIKKSS#4955
# github  : github.com/TRIKKSS
# readme  : github.com/TRIKKSS/CrackMapExec-PingCastle/blob/main/README.md

from impacket.smbconnection import SMBConnection
from os import getcwd


class NXCModule:


	name = 'pingcastle'
	description = 'Execute pingcastle on a remote machine and download the results files'
	supported_protocols = ['smb']
	opsec_safe = True
	multiple_hosts = False


	def options(self, context, module_options):
		"""
			PINGC_PATH    path to the PingCastle executable
			PINGC_CONF    path to the PingCastle config file (optional)
			PINGC_FLAG    flags for the PingCastle executable (optional)
		"""
		if not "PINGC_PATH" in module_options:
			context.log.error('PINGC_PATH option is required!')
			exit(1)

		if "PINGC_CONF" in module_options:
			self.conf = module_options["PINGC_CONF"]
		else:
			self.conf = None

		if "PINGC_FLAG" in module_options:
			self.flags = module_options["PINGC_FLAG"].split(",")
		else:
			self.flags = []

		self.pingcastle_path = module_options["PINGC_PATH"]


	def on_login(self, context, connection):

		# connect to smb
		lmhash = getattr(connection, "lmhash", "")
		nthash = getattr(connection, "nthash", "")
		client = smb_custom("C$", connection.host, connection.domain, connection.username, connection.password, lmhash, nthash)
		
		# upload my executable
		client.upload_file(self.pingcastle_path, "PingCastle.exe")
		if self.conf:
			client.upload_file(self.conf, "PingCastle.exe.config")
		context.log.success("files uploaded")

		# execute PingCastle
		command = f"cd C:\\Windows\\Temp\\ && .\\PingCastle.exe --server {connection.domain} "
		if len(self.flags):
			command += " ".join(self.flags)
		else:
			# if we dont specify flags, pingcastle will be run in interactive mode.
			command += "--healthcheck"
		
		context.log.info(f"executing : {command}")
		print(connection.execute(command, True))
		
		# download result
		try:
			result_filename = f"ad_hc_{connection.domain}."
			client.download_file(result_filename + "xml", f"{getcwd()}/{result_filename}.xml")
			client.download_file(result_filename + "html", f"{getcwd()}/{result_filename}.html")
			context.log.success(f"success ! output files : {getcwd()}/{result_filename}[xml/html]")
		except:
			context.log.error("execution error.")
			client.remove_file("\\Windows\\Temp\\PingCastle.exe")
			if self.conf:
				client.remove_file("\\Windows\\Temp\\PingCastle.exe.config")
			exit(1)

		# remove files
		# to remove : executable, results files, config file
		client.remove_file("\\Windows\\Temp\\" + result_filename + "xml")
		client.remove_file("\\Windows\\Temp\\" + result_filename + "html")
		client.remove_file("\\Windows\\Temp\\PingCastle.exe")
		if self.conf:
			client.remove_file("\\Windows\\Temp\\PingCastle.exe.config")


class smb_custom:
	def __init__(self, address, target_ip, domain, username, password, lmhash, nthash):

		self.share = address
		
		# connect
		self.smbConn = SMBConnection(address, target_ip, sess_port=445)
		self.smbConn.login(username, password, domain, lmhash, nthash)
	

	def upload_file(self,local_filename,destination):
		"""
		param local_filename : path to the local file to upload
		param destination    : destination on the remote machine
		"""
		fh = open(local_filename, "rb")
		self.smbConn.putFile(self.share, f"\\Windows\\Temp\\{destination}", fh.read)
		fh.close()
	

	def download_file(self, filename, destination):
		"""
		param filename    : remote filename
		param destination : destination on your computer
		"""
		fh = open(destination, "wb")
		self.smbConn.getFile(self.share, f"\\Windows\\Temp\\{filename}", fh.write)
		fh.close()


	def remove_file(self, filename):
		self.smbConn.deleteFile("C$", filename)
