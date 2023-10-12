from pathlib import Path
import streamlit as st
from PIL import Image
import datetime

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
achievement_pic = current_dir / "assets" / "achieve2.png"
achievement_2_pic = current_dir / "assets" / "achieve3.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hari"
PAGE_ICON = ":wave:"
NAME = "Harihara Subramanian Ganesh"
DESCRIPTION = """
Senior Developer
"""
EMAIL = "hganesh0786@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/harihara-subramanian-ganesh-57ba71166/",
    "GitHub": "https://github.com/HVtechno",
}
PROJECTS = {
    "🏆 Top Performer Award from ABinBEV" : achievement_pic
}
PROJECTS_2 = {
    "🏆 Beer Shot Award from ABinBEV" : achievement_2_pic
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Get the current year and month
current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month

# Define the start date for counting years of experience
start_date = datetime.date(2015, 9, 1)

# Calculate the number of years of experience
years_of_experience = current_year - start_date.year

# Adjust the years of experience if the current month is before September
if current_month < 9:
    years_of_experience -= 1

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)
    # --- SOCIAL LINKS ---
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
experience_summary = f"""
- ✔️ {years_of_experience} Years experience with various Development roles including Senior Developer/DevOps & Data Engineer/Business Intelligence/Software Engineer.
- ✔️ Strong hands-on experience in Application/Webapps Development, Process Automations, Business Intelligence Analytics & Visualizations.
- ✔️ Microsoft Certified Azure DevOps Developer
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Strong Analytical/Debugging/Troubleshooting skills
"""

st.write('\n')
st.subheader("Experience Summary")
st.write(experience_summary)

# --- SKILLS --- 
st.write('\n')
st.subheader("Tech Stack")
st.write(
    """
- 👩‍💻 Programming: Python(Pandas, Numpy, Streamlit, Matplotlib, Data Automations, API's)
- 👩‍💻 Web Development: Frontend(Reactjs), Backend(Nodejs & Python Flask)
- 👩‍💻 Application Development: VB.NET, VB
- 🗄️  Databases: Azure Databricks, MSSQL, Azure SQL, Oracle
- ☁️ Cloud : Azure DevOps, Google Cloud, Firebase
- 📊 Data Visualization: PowerBi, MS Excel
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Developer | Anheuser-Busch(ABinBev) | Prague, Czech Republic**")
st.write("07/2022 - Present")
st.write(
    """
- ► Lead Progressive Web Application Development : Led development of 2 intricate web apps with React, Node, and Flask, ensuring high functionality and a 100% user engagement increase.
- ► Full Stack Expertise : Led the end-to-end development and maintenance of 2 web applications, databases, and APIs, resulting in 95% fewer integration issues and 100% better performance optimization.
- ► DevOps Management : Manage CI/CD pipelines in Azure DevOps,ensuring efficient, automated, and error-free deployment processes.
- ► Data Transformation and Automation : Harness Python scripts to deploy data transformations and automate workflows within Azure Functions and Azure Databricks Pipelines. This includes data extraction, manipulation, transformation, and loading into SQL databases, as well as in-depth data analysis using Python libraries such as Pandas and Numpy.
- ► Data Engineering Proficiency : Utilize a range of data engineering skills to execute ETL jobs, employing python and SQL to create efficient SQL stored procedures, views and automated data processes.
- ► Azure Cloud Expertise : Leverage Azure cloud services to architect, build and maintain CI/CD pipelines, ensuring the seamless deployment and management of web applications.
- ► Azure functions Wizardry : Implement Azure functions, including timer and http triggers, resulting in 99% streamlined data automations
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Business Intelligence Expert | Anheuser-Busch(ABinBev) | Prague, Czech Republic**")
st.write("08/2019 - 07/2022")
st.write(
    """
- ► Strategic Data Gathering : Excel in collecting business requirements from stakeholders, aligning with KPIs, and organizational goals
- ► Advanced Data Modeling : Leveraging proficiency in Python, with a strong focus on Pandas and NumPy libraries, crafting predictive data models that provide actionable insights and recommendations.
- ► ETL Mastery : Designing, implementing, and maintaining a robust Extract,Transform, Load (ETL) process that transfers data from diverse sources, including SAP GUI, Oracle, MS SharePoint, and Databricks into a centralized data warehouse (Azure SQL Server), using a combination of Python and VBScripts to streamline data integration.
- ► SQL Database Management : Expertise extending to managing and optimizing SQL databases, adept at crafting complex queries, stored procedures, and views, ensuring data retrieval efficiency.
- ► Visual Insights : Skilled in crafting Power BI dashboards and reports,simplifying complex data for informed decisions.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Process Specialist | Infosys BPO s.r.o | Brno, Czech Republic**")
st.write("05/2017 - 06/2019")
st.write(
    """
- ► Document Preparation : Excelling in the preparation of business documents, employing keen attention to detail and validation processes to guarantee their precision and completeness.
- ► Technical Troubleshooting : Troubleshooting inbound trade messages from clients, handling diverse formats such as CSV and FPML to ensure the smooth flow of data and minimize disruptions.
- ► Client Solutions : Bringing expertise in client solutions and fostering collaborative teamwork with application development teams to enhance external client experiences and project efficiency.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Software Engineer - Testing | ATOS(Syntel International PVT.LTD) | Chennai, India**")
st.write("09/2015 - 01/2017")
st.write(
    """
- ► Business Requirement Documents : Proficient in the preparation of Business Requirement Documents (BRD's) for clients, ensuring clarity and precision in project objectives and expectations.
- ► Requirement Analysis and QA : Conducted requirement analysis, created test plans, prepared test cases, executed tests, and reviewed them to ensure thorough coverage for better deliverable quality.
- ► Stakeholder Engagement : Engaged in project sign-up meetings with customers, cross-functional teams, and clients to maintain transparent communication, address concerns, and ensure project success.
"""
)

# --- Certifications ----
st.write('\n')
st.subheader("Certifications & Awards")
st.write("---")
st.write("🏆", "**Microsoft Certified - Azure Data Engineer Associate**")
st.write(
    """
- ► Issued On Jul 2023
- ► Credential ID 48B05988B7337C45
"""
)
st.write('\n')
st.write("🏆", "**Microsoft Certified - Azure Developer Associate**")
st.write(
    """
- ► Issued On Feb 2023
- ► Credential ID 3178BE652FCBDDB8
"""
)
st.write('\n')
st.write("🏆", "**Microsoft Certified - Azure Data Fundamentals**")
st.write(
    """
- ► Issued On Jun 2022
- ► Credential ID 3B89D50D5795920B
"""
)
st.write('\n')
st.write("🏆", "**LinkedIn : Advanced Core Python Code Challenges**")
st.write(
    """
- ► Issued On Jun 2023
"""
)
st.write('\n')
st.write("🏆", "**LinkedIn : Advanced Python working with Data**")
st.write(
    """
- ► Issued On Jun 2023
"""
)
st.write('\n')
st.write("🏆", "**Robotic Process Automation - UIPATH (Beginner to Expert)**")
st.write(
    """
- ► Issued On Apr 2021
"""
)
st.write('\n')
achievement_pic = Image.open(achievement_pic)
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    st.image(achievement_pic, width=520)

st.write('\n')
achievement_2_pic = Image.open(achievement_2_pic)
for project, link in PROJECTS_2.items():
    st.write(f"[{project}]({link})")
    st.image(achievement_2_pic, width=520)

# --- Contact ----
st.write('\n')
with st.container():
    st.header("Get In Touch With Me!")
    st.write("---")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/71f5949b702391928ef227270157d007" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()