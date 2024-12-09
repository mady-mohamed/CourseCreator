# AI Course Creator

This project is an AI-powered tool for generating course materials such as readings, assignments, case studies, and practice project prompts based on chapter summaries from a `.docx` file. use with [Book Summarizer](https://github.com/mady-mohamed/CourseCreator)

## Features

- Upload a `.docx` file containing chapters.
- Split the document into chapters.
- Generate detailed readings, assignments, case studies, and practice project prompts using AI.

## Requirements

- Python 3.x
- `streamlit`
- `python-docx`
- `ollama`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ai-course-creator.git
    cd ai-course-creator
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your API key for Google Generative AI:
    ```sh
    export GEMINI_API_KEY=your_api_key_here
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run main.py
    ```

2. Upload a `.docx` file containing chapters.

3. Select a chapter from the dropdown menu.

4. Click the buttons to generate readings, assignments, case studies, or practice project prompts.

## File Structure

- `main.py`: The main Streamlit app.
- `chapter.py`: Functions for splitting the document into chapters and displaying them.
- `parse.py`: Functions for generating course materials using Google Generative AI.
- `requirements.txt`: List of required Python packages.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
