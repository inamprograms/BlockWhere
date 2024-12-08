import requests
import os
from typing import Dict, List, Optional

class VectaraClient:
    def __init__(self, customer_id: str, corpus_id: str, api_key: str):
        """
        Initialize Vectara API client
        
        :param customer_id: Your Vectara customer ID
        :param corpus_id: The corpus ID you're working with
        :param api_key: Your Vectara API key
        """
        self.base_url = "https://api.vectara.io/v1"
        self.customer_id = customer_id
        self.corpus_id = corpus_id
        self.api_key = api_key  # Ensure this line initializes the api_key attribute
        self.headers = {
            "Content-Type": "application/json",
            "customer-id": customer_id,
            "x-api-key": api_key,
            "Authorization": f"Bearer {api_key}"  # Add Authorization header if needed
            }
        self.jwt_token = self._get_jwt_token()
        self.headers["Authorization"] = f"Bearer {self.jwt_token}" 
              
    def _get_jwt_token(self) -> str:
        """
        Fetch the JWT token from Vectara using the API key.
        """
        token_url = "https://auth.vectara.io/oauth2/token"  # Replace with the correct endpoint if necessary
        response = requests.post(token_url, headers={"x-api-key": self.api_key})
        
        if response.status_code == 200:
            return response.json().get("token")
        else:
            raise Exception("Failed to obtain JWT token: " + response.text)
            
    def index_document(self, document_id: str, text: str, metadata: Optional[Dict] = None) -> Dict:
        """
        Index a document to Vectara
        
        :param document_id: Unique identifier for the document
        :param text: Content of the document
        :param metadata: Optional metadata for the document
        :return: API response
        """
        payload = {
            "documents": [{
                "documentId": document_id,
                "corpusId": self.corpus_id,
                "contents": [{
                    "text": text
                }]
            }]
        }

        if metadata:
            payload["documents"][0]["metadata"] = metadata

        response = requests.post(
            f"{self.base_url}/index",
            headers=self.headers,
            json=payload
        )
        return response.json()


    def search(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Perform a semantic search query
        
        :param query: Search query string
        :param num_results: Number of results to return
        :return: List of search results
        """
        payload = {
            "query": [
                {
                    "query": query,
                    "corpusKey": [
                        {
                            "customerId": self.customer_id,
                            "corpusId": self.corpus_id
                        }
                    ],
                    "numResults": num_results,
                    "contextConfig": {
                        "charsBefore": 100,
                        "charsAfter": 100
                    }
                }
            ]
        }

        response = requests.post(
            f"{self.base_url}/query",
            headers=self.headers,
            json=payload
        )
        return response.json()


def main():
    # Replace these with your actual Vectara credentials
    CUSTOMER_ID = os.getenv('VECTARA_CUSTOMER_ID')
    CORPUS_ID = os.getenv('VECTARA_CORPUS_ID')
    API_KEY = os.getenv('VECTARA_API_KEY')

    # Initialize the Vectara client
    client = VectaraClient(CUSTOMER_ID, CORPUS_ID, API_KEY)
    
    # Example: Index a document
    index_response = client.index_document(
    document_id="doc1", 
    text="Vectara is an AI-powered semantic search platform.",
    metadata={"source": "company_info"}
    )
    
    print("Indexing Response:", index_response)

    # Example: Perform a search
    search_results = client.search("What is Vectara?")
    print("Search Results:", search_results)
    

if __name__ == "__main__":
    main()