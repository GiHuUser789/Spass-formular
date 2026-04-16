print("XSD FILE GELADEN")

from lxml import etree

def validate_xml(xml_string, xsd_path):
    xml_doc = etree.fromstring(xml_string)

    with open(xsd_path, "rb") as f:
        xsd_doc = etree.parse(f)

    schema = etree.XMLSchema(xsd_doc)

    return schema.validate(xml_doc)
