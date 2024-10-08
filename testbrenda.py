# #!/usr/bin/python
# from zeep import Client
# import hashlib

# # wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
# # password = hashlib.sha256("Jeious2468".encode("utf-8")).hexdigest()
# # client = Client(wsdl)
# # parameters = ("siavash.raissi@tufts.edu",password,"ecNumber*2.7.7.7", "generalInformation*", "commentary*", "organism*Mus musculus", "literature*")
# # resultString = client.service.getGeneralInformation(*parameters)
# # print(resultString)


# # testing getMolecularWeight
# import hashlib
# from zeep import Client

# wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
# password = hashlib.sha256("Jeious2468".encode("utf-8")).hexdigest()
# client = Client(wsdl)
# # For enzyme 1.1.1.1
# parameters_1 = ("siavash.raissi@tufts.edu", password, "ecNumber*1.1.1.1", "ic50Value*", "ic50ValueMaximum*", "inhibitor*", "commentary*", "organism*", "ligandStructureId*", "literature*")
# resultString_1 = client.service.getIc50Value(*parameters_1)
# # For enzyme 1.1.1.2
# parameters_2 = ("siavash.raissi@tufts.edu", password, "ecNumber*1.1.1.2", "ic50Value*", "ic50ValueMaximum*", "inhibitor*", "commentary*", "organism*", "ligandStructureId*", "literature*")
# resultString_2 = client.service.getIc50Value(*parameters_2)
# print(resultString_1, resultString_2)


# from zeep import Client
# import hashlib
# wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
# password = hashlib.sha256("Jeious2468".encode("utf-8")).hexdigest()
# client = Client(wsdl)
# parameters = ("siavash.raissi@tufts.edu",password,"ecNumber*1.1.1.1", "kiValue*", "kiValueMaximum*", "inhibitor*", "commentary*", "organism*Homo sapiens", "ligandStructureId*", "literature*")
# resultString = client.service.getKiValue(*parameters)
# print(resultString)

# exec('\nimport hashlib\nfrom zeep import Client\nwsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"\npassword = hashlib.sha256("Jeious2468".encode("utf-8")).hexdigest()\nclient = Client(wsdl)\nparameters = ("siavash.raissi@tufts.edu", password, "ecNumber*1.1.1.1", "role*", "ligand*", "organism*Homo sapiens", "ligandStructureId*")\nresultString = client.service.getLigands(*parameters)\nprint(resultString)\n')

# from zeep import Client
# import hashlib
# wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
# password = hashlib.sha256("Jeious2468".encode("utf-8")).hexdigest()
# client = Client(wsdl)
# parameters = ("siavash.raissi@tufts.edu",password,"ecNumber*1.1.1.1", "organism*Homo sapiens", "tissue*", "commentary*")
# resultString = client.service.getSourceTissue(*parameters)
# print(resultString)

from zeep import Client
import hashlib

wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
password = hashlib.sha256("Jeious2468".encode("utf-8")).hexdigest()
client = Client(wsdl)
# For aspartate aminotransferase in the liver
parameters_liver = ("siavash.raissi@tufts.edu", password, "ecNumber*2.6.1.1", "turnoverNumber*", "turnoverNumberMaximum*", "organism*Liver", "commentary*", "literature*", "ligandStructureId*", "substrate*")
resultString_liver = client.service.getTurnoverNumber(*parameters_liver)

# For aspartate aminotransferase in the heart
parameters_heart = ("siavash.raissi@tufts.edu", password, "ecNumber*2.6.1.1", "turnoverNumber*", "turnoverNumberMaximum*", "organism*Heart", "commentary*", "literature*", "ligandStructureId*", "substrate*")
resultString_heart = client.service.getTurnoverNumber(*parameters_heart)

print("Liver:", resultString_liver)
print("Heart:", resultString_heart)
