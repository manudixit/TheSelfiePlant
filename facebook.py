import base64
import sys

from temboo.Library.Facebook.Publishing import UploadPhoto
from temboo.core.session import TembooSession

print str(sys.argv[1])

# Encode image
with open(str(sys.argv[1]), "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# Create a session with your Temboo account details
session = TembooSession("accountName", "AppName", "TembooAccessToken")

# Instantiate the Choreo
uploadPhotoChoreo = UploadPhoto(session)

# Get an InputSet object for the Choreo
uploadPhotoInputs = uploadPhotoChoreo.new_input_set()

# Set the Choreo inputs
uploadPhotoInputs.set_AccessToken("FacebookAccessToken")

# Set the Album ID 
uploadPhotoInputs.set_AlbumID("FacebookAlbumID")

# Execute the Choreo
uploadPhotoInputs.set_Photo(encoded_string)

# Execute the Choreo
uploadPhotoResults = uploadPhotoChoreo.execute_with_results(uploadPhotoInputs)

# Print the Choreo outputs
print("Response: " + uploadPhotoResults.get_Response())
