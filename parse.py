import google.generativeai as genai
from rich.console import Console
from tornado import template

genai.configure(api_key="AIzaSyCQpB9fhuh7egpKettu31cEqlP5SDiIAAw")
model = genai.GenerativeModel("gemini-1.5-flash")

template_readings = ('''
    "Based on the following chapter summary, create detailed reading material for a course:

**Summary:** {chapter_summary}

Please provide the reading in the following format:

1. **Introduction:** A brief introduction to the chapter and its importance.
2. **Detailed Explanation of Key Concepts:** Break down and explain key concepts mentioned or implied in the summary.
3. **Applications:** Discuss real-world or practical applications of the concepts covered.
4. **Examples and Case Studies:** Include examples or case studies to illustrate the concepts.
5. **Conclusion:** Summarize the key takeaways from the chapter.

"
''')

template_case_study = ('''
    "Based on the following chapter summary, create a detailed example case study for a course:

**Summary:** {chapter_summary}

Please provide the case study details in the following format:

1. **Case Study Title:** A clear and descriptive title for the case study.
2. **Objective:** The learning goals or skills students will develop by analyzing this case study.
3. **Background:** A brief overview of the context or scenario being examined, including relevant historical, social, or economic details.
4. **Problem Statement:** A clear description of the key issue(s) or challenge(s) to be addressed in the case study.
5. **Analysis Questions:** A set of guided questions to help students critically evaluate and analyze the case.
6. **Expected Insights:** Key lessons, insights, or takeaways that students should gain from the case study.
7. **Supplementary Information (Optional):** Any charts, graphs, datasets, or additional readings that could support the analysis.

"
''')

template_assignments = ('''
    "Based on the following chapter summary, create detailed assignments (minimum of 3, but based on each chapters requirements) for a course:

**Summary:** {chapter_summary}

Please provide the assignment details in the following format:

1. **Assignment Title:** A clear and concise title for the assignment.
2. **Objective:** The learning objectives or goals that the assignment aims to achieve.
3. **Instructions:** Step-by-step instructions outlining what students are expected to do.
4. **Required Materials:** Any resources, readings, or materials students need to complete the assignment.
5. **Submission Guidelines:** Details on how and where to submit the assignment, including format requirements and deadlines.
6. **Assessment Criteria:** The criteria and rubric that will be used to evaluate the assignment, including weightage for each component.
7. **Additional Resources (Optional):** Any supplementary resources or references that might help students in completing the assignment.

"
''')

template_project = ('''
    "Based on the following chapter summary, create a detailed practice project for a course:

**Summary:** {chapter_summary}

Please provide the project details in the following format:

1. **Project Title:** A clear and concise title for the project.
2. **Objective:** The learning goals or skills students will develop by completing the project.
3. **Project Description:** A detailed description of the project, including its context, scope, and expected outcomes.
4. **Steps to Complete the Project:** A step-by-step guide to completing the project, including key milestones and deliverables.
5. **Tools and Resources:** Any software, tools, data, or other resources required for the project.
6. **Evaluation Criteria:** The criteria for assessing the project, including weightage for different aspects such as creativity, accuracy, and presentation.
7. **Optional Extensions (Optional):** Additional tasks or challenges for students who want to go beyond the basic requirements.

"
''')

def split_content(content, max_length = 6000):
    return [
        content[i:i + max_length] for i in range(0, len(content), max_length)
    ]

def parse_with_genai(summary_chunks, section):
    if section == "readings":
        template = template_readings
    elif section == 'case-study':
        template = template_case_study
    elif section == "assignments":
        template = template_assignments
    elif section == "project":
        template = template_project

    console = Console()
    results = []

    for i, chunk in enumerate(summary_chunks):
        prompt = template.format(chapter_summary = summary_chunks)
        response = model.generate_content(prompt)
        results.append(response.text)
        print(f"Parsed batch: {i + 1} of {len(summary_chunks)}")

    parsed_content = ''.join(results)
    console.print(parsed_content)
    return parsed_content