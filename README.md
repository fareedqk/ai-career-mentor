# AI Career Mentor

AI Career Mentor is a personal assistant that helps users with their career development through **Job Scanning**, **Skills Analysis**, and **Interview Preparation** (coming soon). It uses **crew.ai** and the **Llama model** to deliver efficient and tailored guidance.

## Features

### 1. Job Scanning
Find relevant job opportunities based on your skills and preferences.
- **Personalized Search**: Jobs matched to your profile.
- **Insights**: Detailed job descriptions and metrics.

### 2. Skills Analysis
Analyze your skills against current job market requirements.
- **Profile-Based**: Upload your resume or career details.
- **Recommendations**: Get suggestions for skill improvement.

### 3. Interview Preparation (Coming Soon)
Simulate interviews and receive feedback to improve your performance.
- **Mock Interviews**: Tailored to your target role.
- **Feedback**: Real-time evaluation and tips.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/aicareermentor.git
    cd aicareermentor
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    ```bash
    export CREWAI_API_KEY='your-api-key-here'
    ```

4. Run the application:
    ```bash
    python main.py
    ```

## Usage

- **Job Scanning**:
    ```bash
    python main.py --scan-jobs --title "Data Scientist"
    ```

- **Skills Analysis**:
    ```bash
    python main.py --analyze-skills --resume "path/to/resume.pdf"
    ```

## Technologies

- **crew.ai** for job scanning and interview simulation.
- **Llama models** for skill matching and analysis.
- **Python** for core development.

## License

This project is licensed under the MIT License.
