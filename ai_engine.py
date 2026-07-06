from openai import OpenAI

class AIEngine:

    def __init__(self,key):

        self.client=OpenAI(
            api_key=key
        )

    def create_slides(self,text):

        prompt=f"""
        Analisis modul berikut:

        {text}

        Buat presentasi:

        Slide 1 Judul
        Slide 2 Tujuan Pembelajaran
        Slide 3 Materi Inti
        Slide 4 Aktivitas
        Slide 5 Refleksi
        Slide 6 Asesmen
        Slide 7 Kesimpulan

        Maksimum 5 poin
        """

        result=self.client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return result.choices[0].message.content