import streamlit as st
st.title (" AI student Assistant ")
st.write("App is starting...")
st.header("planner agent")
subjects=st.text_input("enter subjects")
days=st.number_input("days until exam ",min_value=1)
hours=st.number_input("study hours per day",min_value=1)
def planner_agent(subjects, days):
    subject_list = subjects.split(",")
    plan = {}

    for i in range(days):
        plan[f"Day {i+1}"] = subject_list[i % len(subject_list)].strip()

    return plan
if st.button("Generate Study Plan"):
    plan = planner_agent(subjects, days)

    st.subheader(" Your Study Plan")

    for day, subject in plan.items():
        st.write(f"{day} → {subject}")

    st.success("Plan generated successfully!")
if "math" in subjects.lower():
    st.info(" Tip: Spend extra time on Math if it's a weak subject")
    # Tutor Agent UI
st.header(" Tutor Agent")

topic = st.text_input("Enter topic to learn")

def tutor_agent(topic):
    topic = topic.lower().strip()

    if topic == "":
        return " Please enter a topic."

    elif "python" in topic:
        return """Python:
Python is a beginner-friendly programming language.
It is used in web development, AI, data science, and automation."""

    elif "machine learning" in topic:
        return """Machine Learning:
It allows computers to learn from data and improve automatically.
Used in predictions, recommendations, and AI systems."""

    elif "ai" in topic or "artificial intelligence" in topic:
        return """Artificial Intelligence:
AI helps machines think, learn, and make decisions like humans.
Examples include chatbots and self-driving cars."""

    elif "data science" in topic:
        return """Data Science:
It involves analyzing data to extract useful insights and support decisions."""

    elif "math" in topic:
        return """ Mathematics:
Math helps in solving problems using numbers, formulas, and logic.
It is important for engineering, science, and daily life."""

    else:
        return f""" {topic.title()}:
This is an important concept.
Try learning its basics, examples, and applications step by step."""

if st.button("Explain Topic"):
    explanation = tutor_agent(topic)
    st.markdown(explanation)
    st.success("Explanation generated!")
import streamlit as st

st.set_page_config(page_title="Reminder Agent", layout="centered")

st.title(" Reminder Agent")
st.subheader("Student Study Reminder System")

student_name = st.text_input("Enter your name")
task = st.text_input("Enter your study task")
study_time = st.time_input("Select study time")

def reminder_agent(name, task, time):
    return f"Hello {name} \n\n Reminder: Don't forget to complete '{task}' at {time}."

if st.button("Set Reminder"):
    if student_name and task:
        st.success("Reminder Created Successfully!")
        st.subheader("Your Reminder")
        st.write(reminder_agent(student_name, task, study_time))
    else:
        st.warning("Please enter your name and task.")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20231110/pngtree-abstract-light-colored-paint-texture-background-wallpaper-image_13802780.pngs");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
import streamlit as st
import pandas as pd
from datetime import datetime
import os

file = "data.csv"

# ---------- Load / Save ----------
def load_data():
    if os.path.exists(file):
        return pd.read_csv(file)
    return pd.DataFrame(columns=["Task", "Status", "Time"])

def save_data(df):
    df.to_csv(file, index=False)

# ---------- Page Setup ----------
st.set_page_config(page_title="Tracker Dashboard", layout="wide")

st.title(" Smart Tracker Dashboard")

df = load_data()

# ---------- Sidebar ----------
st.sidebar.header("➕ Add Task")

task = st.sidebar.text_input("Task name")

add = st.sidebar.button("Add Task")

if add:
    if task.strip():
        new = {
            "Task": task,
            "Status": "Pending",
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
        save_data(df)
        st.sidebar.success("Task added!")
    else:
        st.sidebar.warning("Enter a task")

# ---------- Update section ----------
st.subheader("✏️ Update Tasks")

if len(df) > 0:
    col1, col2 = st.columns(2)

    with col1:
        selected = st.selectbox("Select Task", df["Task"].tolist())

    with col2:
        status = st.selectbox("Update Status", ["Pending", "In Progress", "Done"])

    if st.button("Update Task"):
        df.loc[df["Task"] == selected, "Status"] = status
        df.loc[df["Task"] == selected, "Time"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        save_data(df)
        st.success("Updated successfully!")

# ---------- Dashboard view ----------
st.subheader("Task Dashboard")

if len(df) > 0:
    for i, row in df.iterrows():

        status = row["Status"]

        # color tags
        if status == "Done":
            color = "green"
        elif status == "In Progress":
            color = "orange"
        else:
            color = "red"

        st.markdown(f"""
        <div style="
            padding:10px;
            margin:5px;
            border-radius:10px;
            background-color:#f5f5f5;
            border-left:6px solid {color};
        ">
            <b>{row['Task']}</b><br>
            Status: <b>{status}</b><br>
            Updated: {row['Time']}
        </div>
        """, unsafe_allow_html=True)

else:
    st.info("No tasks yet. Add some from sidebar.")

# ---------- Progress ----------
st.subheader(" Progress Overview")

if len(df) > 0:
    st.bar_chart(df["Status"].value_counts())