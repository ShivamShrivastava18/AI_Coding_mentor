# AI Coding Mentor and Model Training Platform

## Overview

The **AI Coding Mentor** is a full-stack application designed to provide coding assistance, including debugging, complexity analysis, and code explanation. It integrates with a fine-tuned **CodeLlama-7b** model, optimized for these tasks using state-of-the-art techniques like 4-bit quantization and Low-Rank Adaptation (LoRA).

## Features

### Coding Mentor
- **Debugging**: Automatically detects errors in code and suggests fixes.
- **Code Conversion**: Translates code between programming languages (e.g., Python ↔ Java).
- **Complexity Analysis**: Evaluates time and space complexity, offering optimization tips.
- **Code Explanation**: Breaks down and explains code functionality line-by-line.

### Model Training Script
- Fine-tunes the **CodeLlama-7b** model using Hugging Face Transformers.
- Implements 4-bit quantization for efficient training.
- Uses LoRA for parameter-efficient tuning, targeting key layers.

## Tech Stack
- **Backend**: Python, Hugging Face, LangChain, Flask
- **Frontend**: Streamlit

## Setup and Installation

### Prerequisites
- Python 3.8+
- Docker (for containerized deployment)
- GPU (for model training)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-coding-mentor.git
   cd ai-coding-mentor
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

5. (Optional) For model training, execute:
   ```bash
   python train_model.py
   ```

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t ai-coding-mentor .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 ai-coding-mentor
   ```

## Usage

### Coding Mentor
- Access the Streamlit app at `http://localhost:8501`.
- Select a feature from the sidebar and input your code to get assistance.

### Model Training
- Edit the `train_model.py` script to configure your dataset or parameters.
- Run the script to fine-tune the model.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **Hugging Face** for their incredible Transformers library.
- **Streamlit** for the interactive UI framework.
- **LangChain** for simplifying the integration of language models.

---

### Future Enhancements

- Add persistent storage for user queries and responses.
- Expand support for additional programming languages.
- Implement real-time collaboration features for team-based coding.

Feel free to reach out or submit issues for any feedback or suggestions!
