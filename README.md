# Soft Skill Analysis from Interviews

This project analyzes soft skills from interview data using machine learning and natural language processing techniques.

## Structure

- `data/`: Contains datasets in raw, processed, and labeled formats.
- `models/`: Trained machine learning models and checkpoints.
- `src/`: Source code for preprocessing, feature extraction, model training, and inference.
- `audio_processing/` and `video_processing/`: Scripts for converting audio and video into analyzable data.
- `app/`: Contains files for API deployment and configuration.
- `tests/`: Unit and integration tests for code reliability.
- `logs/`: Stores log files for tracking process outputs and errors.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dsmita03/Soft_Skill
   cd Soft_Skill

2. Install dependencies:

   ```bash 
    pip install -r app/requirements.txt
    ```

3. Run tests:

   ```bash
   python -m unittest discover -s tests
   ```

4. Start the API:

   ```bash
   python app/wsgi.py
   ```
   