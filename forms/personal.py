import streamlit as st
from validation.regex_checks import is_valid_email, is_valid_plz

def render_personal_form():
    st.subheader("Persönliche Daten")

    st.text_input("Vorname", key="first_name")
    st.text_input("E-Mail", key="email")
    st.text_input("PLZ", key="plz")

    if st.button("Validiere Eingaben"):
        errors = []

        if not st.session_state.first_name:
            errors.append("Vorname fehlt")

        email = st.session_state.email
        if not email:
            errors.append("E-Mail fehlt")
        elif not is_valid_email(email):
            errors.append("E-Mail ungültig")

        plz = st.session_state.plz
        if not plz:
            errors.append("PLZ fehlt")
        elif not is_valid_plz(plz):
            errors.append("PLZ ungültig")

        if errors:
            for e in errors:
                st.error(e)
        else:
            st.success("Frontend-Validierung OK")
