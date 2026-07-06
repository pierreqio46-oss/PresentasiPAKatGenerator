import requests
import tempfile
import base64

class ImageGenerator:

    def __init__(self,client):

        self.client=client


    def create(self,topic):

        result=self.client.images.generate(
            model="gpt-image-1",
            prompt=f"""
            Ilustrasi pendidikan
            agama katolik:

            {topic}
            """
        )

        image_base64=result.data[0].b64_json

        image_data=base64.b64decode(
            image_base64
        )

        path=tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        ).name

        with open(path,"wb") as f:
            f.write(image_data)

        return path