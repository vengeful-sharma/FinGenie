import streamlit as st
import sqlite3
from datetime import datetime

# Check if the user is logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to continue with FinGenie.")
    st.stop()

user_email = st.session_state.user_email

st.title("Write Note")

# Connect to the database
conn = sqlite3.connect("notes.db")
c = conn.cursor()

# Create the notes table if it doesn't exist
c.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        note TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# Add 'edited' column if it's missing (helpful for tracking changes)
try:
    c.execute("ALTER TABLE notes ADD COLUMN edited BOOLEAN DEFAULT 0")
    conn.commit()
except sqlite3.OperationalError:
    pass  # Column already exists, no problem

# Input for new note
note_text = st.text_area("Write your note here:")

if st.button("Save Note"):
    if note_text.strip():
        c.execute("INSERT INTO notes (user_email, note) VALUES (?, ?)", (user_email, note_text))
        conn.commit()
        st.success("Note saved!")
        st.rerun()
    else:
        st.error("Note is empty!")

# Show existing notes
st.subheader("Your saved notes")
c.execute("SELECT id, note, timestamp, edited FROM notes WHERE user_email = ? ORDER BY timestamp DESC", (user_email,))
rows = c.fetchall()

if rows:
    for note_id, note, timestamp, edited in rows:
        # Format the timestamp nicely
        try:
            formatted_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f").strftime("%b %d, %Y at %I:%M %p")
        except ValueError:
            formatted_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime("%b %d, %Y at %I:%M %p")

        with st.expander(f"{formatted_time} {'(edited)' if edited else ''}"):
            edited_note = st.text_area(f"Edit Note #{note_id}", note, key=f"edit_{note_id}")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("Update", key=f"update_{note_id}"):
                    if edited_note.strip():
                        c.execute(
                            "UPDATE notes SET note = ?, timestamp = ?, edited = 1 WHERE id = ?",
                            (edited_note, datetime.now(), note_id)
                        )
                        conn.commit()
                        st.success("Note updated.")
                        st.rerun()
                    else:
                        st.error("Note cannot be empty.")
            with col2:
                if st.button("Delete", key=f"delete_{note_id}"):
                    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
                    conn.commit()
                    st.warning("Note deleted.")
                    st.rerun()
else:
    st.info("No notes found.")

conn.close()
