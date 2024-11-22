import streamlit as st

def generate_project_outputs(name, pitch, description):
    """Generate 10 variations of project details based on the input."""
    projects = []
    for i in range(1, 11):
        projects.append({
            "name": f"{name} - Variation {i}",
            "pitch": f"{pitch} (Improved Pitch {i})",
            "description": f"{description} (Enhanced Description {i})"
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
        
        # Display results
        st.subheader("Generated Projects")
        for i, project in enumerate(project_outputs, start=1):
            st.write(f"### Project {i}")
            st.write(f"**Name:** {project['name']}")
            st.write(f"**Pitch:** {project['pitch']}")
            st.write(f"**Description:** {project['description']}")
    else:
        st.error("Please fill in all fields before generating.")
