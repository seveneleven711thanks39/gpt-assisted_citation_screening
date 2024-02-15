#!/usr/bin/env python
# coding: utf-8

# Define a function to create the 'screening' text
def create_screening_text(row):
    screening_text = (
        "You are conducting a systematic review and meta-analysis, focusing on a specific area of medical research. "
        "Your task is to evaluate research studies and determine whether they should be included in your review. "
        "To do this, each study must meet the following criteria:\n\n"
        "Target Patients: The study includes adult patients (18 years old or older) with sepsis, or suspected as sepsis, infection, bacteremia or patients admitted to ICU.\n" 
        "Intervention: The study investigates the effects of targeting a higher mean arterial pressure.\n"
        "Comparison: The study compares the above intervention with a strategy of targeting a lower mean arterial pressure.\n"
        "Study Design: The study must be a randomized controlled trial.\n"
        "Additionally, any study protocol that meets these criteria should also be included.\n\n"
        "However, you should exclude studies in the following cases:\n\n"
        "The study does not meet all of the above eligibility criteria.\n"
        "The study's design is not a randomized controlled trial. Examples of unacceptable designs include case reports, " 
        "observational studies, systematic reviews, review articles, animal experiments, letters to editors, and textbooks.\n"
        "After reading the title and abstract of a study, decide whether to include or exclude it based on these criteria. "
        "When judging each domain, if there is uncertainty in the decision due to a lack of adequate information, please answer "
        "with include in order to minimize the possibility of falsely excluding potentially relevant literature. "
        "Please answer the question with include or exclude only.\n\n"
    )
    # Append the title
    screening_text += f"Title: {row['title']}\n\n"
    # Append the abstract if it exists
    if not pd.isna(row['abstract']):
        screening_text += f"Abstract: {row['abstract']}\n\n"
    return screening_text

# Apply the function to each row
df['screening'] = df.apply(create_screening_text, axis=1)

# Execute the script to save the DataFrame to an Excel file
df.to_excel("Path to your file")
