from bing_image_downloader import downloader
def search(name):
    query_string = name
    downloader.download(query_string, limit=3,  output_dir='C:/Users/467/Documents/gsearch',
    adult_filter_off=True, force_replace=False, timeout=60)
