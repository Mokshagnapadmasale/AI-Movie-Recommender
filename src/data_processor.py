import pandas as pd


class MovieDataProcessor:
    
    def __init__(self,original_csv,processed_csv):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_process_movie_data(self):
        dataset = pd.read_csv(filepath_or_buffer=self.original_csv,encoding='utf-8')
        dataset.drop_duplicates(inplace=True,ignore_index=True)
        required_columns = {'title','description','cast','director','genre','release_date','keywords'}
        missing = required_columns - set(dataset.columns)
        if missing:
            raise ValueError('Missing some colums')
        else:
            dataset['combined_info'] = (
        " Title: " + dataset['title'] + " description: " + dataset["description"] + " Cast: " + dataset['cast'] + " Director : " + dataset['director'] + " Genre: " + dataset['genre'] + " Release-Date : " + dataset['release_date'] + " Keywords: " + dataset['keywords']
        )
        dataset[['combined_info']].to_csv(path_or_buf=self.processed_csv,index=False,encoding='utf-8')
        return self.processed_csv
