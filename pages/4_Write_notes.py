import streamlit as st
import sqlite3

# Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to continue with FinGenie.")
    st.stop()

user_email = st.session_state.user_email

st.title("Write Note")

# Connect to notes database
conn = sqlite3.connect("notes.db")
c = conn.cursor()

# Create table if not exists
c.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        note TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# Note input area
note_text = st.text_area("Write your note here:")

if st.button("Save Note"):
    if note_text.strip():
        c.execute("INSERT INTO notes (user_email, note) VALUES (?, ?)", (user_email, note_text))
        conn.commit()
        st.success("Note saved!")
    else:
        st.error("Note is empty!")

# Display saved notes for this user
st.subheader("Your saved notes")
c.execute("SELECT note, timestamp FROM notes WHERE user_email = ? ORDER BY timestamp DESC", (user_email,))
rows = c.fetchall()

if rows:
    for note, timestamp in rows:
        st.markdown(f"- **{timestamp}**: {note}")
else:
    st.info("No notes found.")

conn.close()
