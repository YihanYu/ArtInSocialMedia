from google.cloud import vision
from google.cloud.vision.feature import Feature
from google.cloud.vision.feature import FeatureTypes

client = vision.Client.from_service_account_json('keyfile.json')

def googleAPI(uri):
    """Detects image properties in the file."""
    image = client.image(source_uri=uri)

    props = image.detect_properties()
    colors=[]
    if props is not None:
        for color in props.colors:
            rgbScore = []
            rgbScore.append(color.color.red)
            rgbScore.append(color.color.green)
            rgbScore.append(color.color.blue)
            rgbScore.append(color.pixel_fraction)
            colors.append(rgbScore)
        return colors
    else:
        return colors

print googleAPI('https://cdn.dribbble.com/users/823823/screenshots/2365098/045_2.gif')
