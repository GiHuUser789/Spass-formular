def create_xml(data):
    return f"""
    <person>
        <first_name>{data.get('first_name', '')}</first_name>
        <email>{data.get('email', '')}</email>
        <plz>{data.get('plz', '')}</plz>
    </person>
    """
