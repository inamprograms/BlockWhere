import os
from vectara_RAG import VectaraRAG
if __name__ == "__main__":
    rag = VectaraRAG()
    corpus_id = os.getenv("VECTARA_CORPUS_ID")
    while True:
        print("\nChoose an action:")
        print("1. Create a new corpus")
        print("2. Reset the current corpus")
        print("3. Upload a file to the current corpus")
        print("4. Query Vectara")
        print("5. Ask question with to llm with summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            corpus_name = input("Enter the name for the new corpus: ")
            corpus_id = rag.create_corpus(corpus_name)
            print("Corpus created with ID:", corpus_id)

        elif choice == "2":
            rag.reset_corpus(corpus_id)
            print("Corpus reset successfully.")

        elif choice == "3":
            file_path = input("Enter the path of the file to upload: ")
            rag.upload_data(corpus_id, file_path)
            print("File uploaded successfully.")

        elif choice == "4":
            question = input("Enter your question: ")
            top_k = int(input("Enter the number of results to return: "))
            lang = input("Enter the language (default is 'en'): ") or "en"
            summary = rag.query_vectara(corpus_id, question, top_k=top_k, lang=lang)
            print("vectara_Summary:", summary)

        elif choice == "5":
            question = input("Enter your question: ")
            top_k = int(input("Enter the number of results to return: "))
            lang = input("Enter the language (default is 'en'): ") or "en"
            summary = rag.query_vectara(corpus_id, question, top_k=top_k, lang=lang)
            print("Vectara_Summary:", summary)
            answer = rag.ask_question_with_summary(summary, question)
            print("LLM_Answer:", answer)


        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")
