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
    # 📘 Tutor Agent UI
st.header("📘 Tutor Agent")

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
