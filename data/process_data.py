import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    Load and join input raw data   
    """

    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, how ='outer', on =['id'])
    return df


def clean_data(df):
    """
    Clean the dataframe.
    """
    categories = df['categories'].str.split(";", expand=True)
    row = categories.iloc[0]
    category_colnames = [x.split("-")[0] for x in row]
    categories.columns = category_colnames
    
    for column in categories:
        # Set each value to be the last character of the string
        categories[column] = categories[column].str.split("-").str[-1]
        # Convert column from string to numeric
        categories[column] = categories[column].apply(pd.to_numeric)
    
    df = df.drop("categories", axis=1)    
    # Concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], sort=False, axis=1)
    # Drop duplicates
    df = df.drop_duplicates()

    return df


def save_data(df, database_filename):
    """
    Save the cleaned dataframe into database.
    """
    engine = create_engine(f'sqlite:///{database_filename}')
    df.to_sql('Project2', engine, index=False, if_exists='replace')  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()