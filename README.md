# Large language model-assisted citation screening

This project demonstrates how to load data from an Excel file, generate screening texts based on specific criteria, and integrate with OpenAI's GPT-4 API for automated ciation screening.

## Features

- Data loading and processing with Pandas and Openpyxl.
- Text generation based on predefined criteria.
- Integration with OpenAI's GPT-4 API for automated citation screening.

## Prerequisites

- Python 3.x
- An OpenAI API key with access to GPT-4.

## Installation

1. Clone the repository:
2. Install the required dependencies:

## Usage

- Update `data_loader.py` with your Excel file's directory and name.
- Define your criteria in `screening_text_generator.py`.
- Set your OpenAI API key in `gpt_integration.py`.
- Run the scripts in the following order:
1. `python data_loader.py`
2. `python screening_text_generator.py`
3. `python gpt_integration.py`

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
