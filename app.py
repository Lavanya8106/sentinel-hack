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