import streamlit as st
from forms.personal import render_personal_form
from export.xml_export import create_xml
from validation.xsd_validation import validate_xml
from export.json_export import create_json
import json
from api.api_client import send_data_to_api
from database.db_operations import create_table, insert_person, get_all_persons



st.title("Formular App")
create_table()


render_personal_form()

st.divider()

data = st.session_state

# 🔹 XML
if st.button("XML erstellen & prüfen"):
    xml = create_xml(data)

    st.subheader("XML:")
    st.code(xml)

    is_valid = validate_xml(xml, "config/person.xsd")

    if is_valid:
        st.success("XML ist gültig!")
    else:
        st.error("XML ist NICHT gültig!")

# 🔹 JSON anzeigen
if st.button("JSON anzeigen"):
    json_data = create_json(data)

    st.subheader("JSON:")
    st.json(json_data)

# 🔹 JSON Download (OHNE extra Button)
json_data = create_json(data)
json_string = json.dumps(json_data, indent=2)

st.download_button(
    label="Download JSON",
    data=json_string,
    file_name="data.json",
    mime="application/json"
)

if st.button("Daten an API senden"):
    data = st.session_state

    response = send_data_to_api(data)

    st.subheader("Status:")
    st.write(response.status_code)

    st.subheader("Antwort:")
    st.json(response.json())

if st.button("In DB speichern"):
    insert_person(st.session_state)
    st.success("Gespeichert!")

if st.button("Daten anzeigen"):
    rows = get_all_persons()

    data_list = []
    for row in rows:
        data_list.append({
            "id": row[0],
            "first_name": row[1],
            "email": row[2],
            "plz": row[3]
        })

    st.dataframe(data_list)

def delete_person(person_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM persons WHERE id = ?", (person_id,))

    conn.commit()
    conn.close()

st.subheader("Datensatz löschen")

delete_id = st.number_input("ID zum Löschen", step=1)

if st.button("Löschen"):
    delete_person(delete_id)
    st.success("Gelöscht!")

def update_person(person_id, data):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE persons
        SET first_name = ?, email = ?, plz = ?
        WHERE id = ?
    """, (
        data.get("first_name"),
        data.get("email"),
        data.get("plz"),
        person_id
    ))

    conn.commit()
    conn.close()

st.subheader("Datensatz bearbeiten")

update_id = st.number_input("ID zum Bearbeiten", step=1)

if st.button("Aktualisieren"):
    update_person(update_id, st.session_state)
    st.success("Aktualisiert!")

rows = get_all_persons()

for row in rows:
    st.write(row)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"Löschen {row[0]}"):
            delete_person(row[0])

    with col2:
        if st.button(f"Bearbeiten {row[0]}"):
            st.session_state.first_name = row[1]
            st.session_state.email = row[2]
            st.session_state.plz = row[3]
