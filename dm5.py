class Package(object):
	def __init__(self, ecosystem="", package_name=""):
		self.ecosystem = ecosystem
		self.package_name = package_name


class Version(Package):
	def __init__(self, Package, version="",sha="", authored_by=[], contributed_by=[], depends_on=[], similar_to=[]):
		self.ecosystem = Package.ecosystem
		self.package_name = Package.package_name
		self.version = version
		self.sha = sha
		self.authored_by = authored_by
		self.contributed_by = contributed_by
		self.depends_on = []
		self.similar_to = []


	def version_depends_on(self, Version, dependency_type=None):
		self.depends_on.append({"version":Version.sha, "dependency_type" : dependency_type})


	def version_similar_to(self, Version, score=None):
		self.similar_to.append({"version":Version.sha, "score" : score})


class UsageDetails(Version):
	pass


class SecurityDetails(object):
	pass

class LicenseDetails(object):
	pass


class TechnicalDebt(object):
	pass