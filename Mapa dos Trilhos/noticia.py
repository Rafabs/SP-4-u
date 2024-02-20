from GoogleNews import GoogleNews
import pandas as pd

def notice_transp_sao_paulo():
    googlenews = GoogleNews(period='d')
    googlenews.setlang('pt')
    googlenews.search('Transporte Público São Paulo')
    result = googlenews.result()

    # Verifica se há resultados antes de criar o DataFrame
    if result:
        df = pd.DataFrame(result)
        df_filtered = df[['title', 'link', 'date', 'desc', 'media', 'datetime', 'img']].head(50)
        return df_filtered
    else:
        print("Nenhuma notícia encontrada.")
