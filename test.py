import sys

sys.path.append('./class')
from ConfigParserJson import configParserJson

#ConfigParserJson = configParserJson()

config = configParserJson().originatorImporter['smsc']

print(config['operators'])