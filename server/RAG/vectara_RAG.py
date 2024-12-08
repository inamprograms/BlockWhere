from vectara import vectara
from dotenv import load_dotenv
import os
import openai
from openai import OpenAI
import requests
import json
# from consts.prompts import promptProductOptimization

class VectaraRAG:
    def __init__(self):
        """
        Initialize the Vectara client.
        """
        load_dotenv()
        self.customer_id = os.getenv("VECTARA_CUSTOMER_ID")
        self.api_key = os.getenv("VECTARA_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def create_client(self):
        """
        Create a Vectara client.
        """
        return vectara(self.customer_id, self.api_key, from_cli=False)

    def create_corpus(self, corpus_name):
        """
        Create a new corpus.
        """
        client = self.create_client()
        return client.create_corpus(corpus_name)

    def reset_corpus(self, corpus_id):
        """
        Reset a corpus.
        """
        client = self.create_client()
        client.reset_corpus(corpus_id)
    
    def delete_corpus(self, corpus_id):

        url = "https://api.vectara.io/v1/delete-corpus"

        payload = json.dumps({
        "corpusId": corpus_id
        })
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': self.api_key
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        res = json.loads(response.text)
        res = res["status"]["statusDetail"]
        return res

    def upload_data(self, corpus_id, file_path):
        """
        Upload data to a corpus.
        """
        client = self.create_client()
        client.upload(corpus_id, file_path)

    def query_vectara(self, corpus_id, question, top_k=20, lang="en"):
        """
        Query the Vectara engine.
        """
        client = self.create_client()
        response = client.query(corpus_id, question, top_k=top_k, lang=lang)
        summary = response['responseSet'][0]['summary'][0]['text']
        return summary

    def ask_question_with_summary(self, summary, question):
        """
        Ask a question with a summary.
        """
        openai.api_key=self.openai_api_key
        client = OpenAI()
        completion = client.chat.completions.create(
            # model="gpt-3.5-turbo",
            model="gpt-4o",
            messages=[
                {"role": "user",
                "content": 
                f"Follow these instructions: add bracesfor variable\n"
                f"We have provided you the description of the \n"
                f"---------------------\n"
                f"{summary}"
                f"\n---------------------\n"
                f"Follow the instructions and use description provided then answer this : {question}"
                }
            ]
        )

        return completion.choices[0].message.content