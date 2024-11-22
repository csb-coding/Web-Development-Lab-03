import streamlit as st
import info
import pandas as pd

def abt_me_section():
    st.header("About Me")
    st.write(" ")
    st.image(info.profile_picture, width=500)
    st.write(" ")
    st.write(info.about_me)
    st.write("---")
abt_me_section()

def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt = "Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt = "Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Expected Graduation']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I learned"},
        hide_index=True,
        )
    st.write("---")
education_section(info.education_data, info.course_data)

def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience_section(info.experience_data)

def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"project_name")
        expander.write(project_description)
    st.write("---")
project_section(info.projects_data)

def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        icon = info.programming_icons.get(skill, '')
        st.write(f"{skill}{icon}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        spoken_icons = info.spoken_icons.get(spoken, '')
        st.write(f"{spoken}{spoken_icons}: {proficiency}")
    st.write("---")
skills_section(info.programming_data, info.spoken_data)

def activities_section(leadership_data, activity_data):
    st.header("Activites")
    tab1, tab2 = st.tabs(["Involvement", "Community Service"])
    with tab1:
        st.subheader("Involvement")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=450)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, detail in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in detail:
                expander.write(bullet)
    st.write("---")
activities_section(info.leadership_data, info.activity_data)
