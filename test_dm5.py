'''
How to run the test
install pytest
make sure you have test_dm5.py and dm5.py in the same folder.
python2 -m py.test test_dm5.py
'''
from dm5 import Package, Version

my_package1 = Package("NPM", "express")
my_package2 = Package("NPM", "node")

my_version1 = Version(my_package1, "1.0.0", sha="abc123", authored_by=[], contributed_by=[], depends_on=[], similar_to=[])
my_version2 = Version(my_package2, "1.1.0", sha="bbe1234", authored_by=[], contributed_by=[], depends_on=[], similar_to=[])

my_version1.version_depends_on(my_version2,"runtime dependency")

my_version2.version_similar_to(my_version1,"0.02")


def test_package_name():
	assert my_package1.package_name == "express"


def test_match_ecosystem():
	assert my_package1.ecosystem == my_package2.ecosystem


def test_dependency():
 	dep = my_version1.depends_on[0]
 	assert dep["version"] == my_version2.sha and dep["dependency_type"] == "runtime dependency"

def test_similarity():
	sim = my_version2.similar_to[0]
	assert sim["version"] == my_version1.sha and sim["score"] == "0.02"