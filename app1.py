import streamlit as st
import pandas as pd
from io import StringIO

def generate_project_outputs(name, pitch, description):
    """Generate 10 variations of project details based on the input."""
    projects = []
    for i in range(1, 11):
        projects.append({
            "Name": f"{name} - Variation {i}",
            "Pitch": f"{pitch} (Improved Pitch {i})",
            "Description": f"{description} (Enhanced Description {i})"
        })
    return projects

# Streamlit App
st.title("Project Idea Generator")

# Pre-fill Dummy Data
if st.checkbox("Use Dummy Data"):
    project_name = "GreenTech AI"
    project_pitch = "An AI-driven platform to optimize renewable energy usage and reduce carbon footprints."
    project_description = "GreenTech AI leverages machine learning and IoT to analyze energy consumption patterns and suggest eco-friendly solutions tailored to businesses and individuals."
else:
    # Input Fields
    project_name = st.text_input("Project Name:", placeholder="Enter the name of your project")
    project_pitch = st.text_area("Project Pitch:", placeholder="Enter the pitch for your project")
    project_description = st.text_area("Project Description:", placeholder="Enter a brief description of the project")

# Send Button
if st.button("Generate"):
    if project_name and project_pitch and project_description:
        # Generate output
        project_outputs = generate_project_outputs(project_name, project_pitch, project_description)
        df = pd.DataFrame(project_outputs)  # Convert to DataFrame
        
        # Display results in a table
        st.subheader("Generated Projects")
        st.dataframe(df)
        
        # Prepare CSV download
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        
        # Download button
        st.download_button(
            label="Download CSV",
            data=csv_buffer.getvalue(),
            file_name="generated_projects.csv",
            mime="text/csv"
        )
    else:
        st.error("Please fill in all fields before generating.")

