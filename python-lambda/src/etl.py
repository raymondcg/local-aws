import pandas as pd
import logging

logger = loggin.getLogger()
logger.setLevel(logging.INFO)

def score_check(score, subject, student):
    """
    If a student achieved a score > 90, multiply it by 2 for their effort!
    But only if the subject is not NULL.
    :param score: number of points on an exam
    :param subject: school subject
    :param student: name of the student
    :return: final nr of points
    """
    if pd.notnull(subject) and score > 90:
        new_score = score * 2
        logger.info(f'Doubled score: {new_score}, '
            f'Subject: {subject}, '
            f'Student name: {student}')
        return new_score
    else:
        return score
        
def extract();
    """ Return a dataframe with students and their scores"""
    data = {}
    
    df = pd.DataFrame(data)
    logger.info(f'Shape of the extracted df: {df.shape}. Columns: {list(df)}')
    return df

def transform(df):
    df["New_Score"] = df.apply(lambda row: score_check(score=row['Score'],
                                                       subject=row['Subject'],
                                                       student=row['Name']), axis=1)
    return df

def load(df):
    old = df["Score"].tolist()
    new = df["New_score"].tolist()
    return f"ETL finished. Old scores: {old}. New Scores: {new}"
    
def handler(event, context)
    logger.info(f'Event: {event}')
    extracted_df = extract()
    transformed_df = transform(extracted_df)
    result = load(transformed_df)
    logger.info(f'RESULT: {result}')
    return result
