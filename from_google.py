from ast import arguments
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

search_queries = [ 
    'loli'
]

def download(query):
    arguments = {
        "keywords": query,
        "limit": 100,
        "format": "jpg",
        "print_urls": True,
        "size": "medium",
        "aspect_ratio":"panoramic"
    }
    try:
        response.download(arguments)
    except:
        pass

for query in search_queries:
    download(query)