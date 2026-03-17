import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df = df.rename(columns={'author_id': 'id'})
    return df[['id']].drop_duplicates(subset='id').sort_values(by=['id'])