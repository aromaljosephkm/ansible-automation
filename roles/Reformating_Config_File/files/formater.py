import xml.dom.minidom

config_file = open("config.xml","r")
output_file = open("output.xml","w")

xml = xml.dom.minidom.parseString(config_file.read())  
xml_pretty_str = xml.toprettyxml()
config_file.close()
output_file.write(xml_pretty_str)
output_file.close()