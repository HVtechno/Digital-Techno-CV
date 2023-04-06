from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
achievement_pic = current_dir / "assets" / "achieve2.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hari"
PAGE_ICON = ":wave:"
NAME = "Harihara Subramanian Ganesh"
DESCRIPTION = """
DevOps Engineer
"""
EMAIL = "hganesh0786@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/harihara-subramanian-ganesh-57ba71166/",
    "GitHub": "https://github.com/HVtechno",
}
PROJECTS = {
    "🏆 Top Performer Award from ABinBEV" : achievement_pic
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


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
st.subheader("Experience Summary")
st.write(
    """
- ✔️ 7 Years experience with various Development roles including DevOps Engineer/Buisness Intelligence/Software Engineer.
- ✔️ Strong hands on experience in Application/Web Development, Process Automations, Business Intelligence Analytics & Visualizations.
- ✔️ Microsoft Certified Azure DevOps Developer
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Strong Analytical/Debugging/Troubleshooting skills
"""
)

# --- SKILLS --- 
st.write('\n')
st.subheader("Tech Stack")
st.write(
    """
- 👩‍💻 Web Development: Frontend(Reactjs), Backend(Nodejs)
- 👩‍💻 Programming: Python, VB, VB.NET
- 🗄️  Databases: MSSQL, Azure SQL, Oracle
- ☁️ Cloud : Azure DevOps
- 📊 Data Visualization: PowerBi, MS Excel
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**DevOps Engineer | Anheuser-Busch(ABinBev) | Prague, Czech Republic**")
st.write("07/2022 - Present")
st.write(
    """
- ► Acting as Senior Developer and responsible to build complex web applications using Reactjs & Nodejs
- ► Developing and maintaining web applications, databases & APIs.
- ► Managing CI & CD pipelines in Azure DevOps
- ► Developing & deploying Python scripts to Azure Functions, Azure Databricks Pipelines to perform necessary data transformations & automate workflows.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Business Intelligence Expert | Anheuser-Busch(ABinBev) | Prague, Czech Republic**")
st.write("08/2019 - 07/2022")
st.write(
    """
- ► Gathered Business Requirements from stakeholders to understand their data analysis needs and identified the key performance indicators.
- ► Developed predictive data models & analyzed using python (Pandas, NumPy)
- ► Build and maintained ETL process that transfer data from sources like SAP GUI/Oracle/MS SharePoint/Databricks into centralized data warehouse (MSSQL Server) using Python/VBScripts.
- ► Managed and optimized SQL databases (Complex SQL Queries/Stored Procedures/Views)
- ► Created dashboards and reports that visualize data insights & KPIs in a clear and concise manner using power BI.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Process Specialist | Infosys BPO s.r.o | Brno, Czech Republic**")
st.write("05/2017 - 06/2019")
st.write(
    """
- ► Experienced in business document preparations, validated functional specifications and analyzed user acceptance test cases through sales force & JIRA.
- ► Troubleshooted clients inbound trade messages in (CSV & FPML) formats.
- ► Worked as subject matter expertise and provided technical solutions to external clients.
- ► Worked closely with various application development teams and escalated client's issue to resolved quickly.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Software Engineer | ATOS(Syntel International PVT.LTD) | Chennai, India**")
st.write("09/2015 - 01/2017")
st.write(
    """
- ► Experienced in preparing client's Business Requirement Documents (BRD's Requirement analysis, Test Pan Creation, Test Case preparation and Test Execution
- ► Involved in Reviewing Test Cases and Manual Walkthrough of Test cases.
- ► Project sign-up meetings with customer & Functional team on daily progress
- ► Coordinate the client calls from offshore & present the detailed reports to customer about the testing activities.
"""
)

# --- Certifications ----
st.write('\n')
st.subheader("Certifications & Awards")
st.write("---")
st.write("🏆", "**Microsoft Certified - Azure DevOps Developer Associate**")
st.write(
    """
- ► Issued On Feb 2023
- ► Credential ID 1596-3046
"""
)
st.write('\n')
st.write("🏆", "**Microsoft Certified - Azure Data Fundamentals**")
st.write(
    """
- ► Issued On Jun 2022
- ► Credential ID 1310-7181
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