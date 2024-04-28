
import tkinter as tk
from tkinter import messagebox
from neo4j import GraphDatabase

# Connection details
uri = "bolt://localhost:7687"
username = "neo4j"
# password = "password"  # replace with your password

# uri = "bolt://localhost:7687"
# username = "neo4j"
password = "masaladosa"

class ResearchPapersDB:
    def __init__(self, master):
        self.master = master
        master.title("Research Papers Database")

        # Initialize the Neo4j connection
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

        # GUI Setup
        self.label_paper_a_id = tk.Label(master, text="Paper A ID:")
        self.entry_paper_a_id = tk.Entry(master)
        self.label_paper_b_id = tk.Label(master, text="Paper B ID:")
        self.entry_paper_b_id = tk.Entry(master)
        self.check_citation_button = tk.Button(master, text="Check Citation", command=self.check_citation)
        self.label_result = tk.Label(master, text="")

        self.label_paper_id = tk.Label(master, text="Paper ID for Classification:")
        self.entry_paper_id = tk.Entry(master)
        self.check_classification_button = tk.Button(master, text="Check Classification", command=self.check_classification)
        self.label_classification = tk.Label(master, text="")

        # Layout
        self.label_paper_a_id.grid(row=0, column=0)
        self.entry_paper_a_id.grid(row=0, column=1)
        self.label_paper_b_id.grid(row=1, column=0)
        self.entry_paper_b_id.grid(row=1, column=1)
        self.check_citation_button.grid(row=2, column=0, columnspan=2)
        self.label_result.grid(row=3, column=0, columnspan=2)

        self.label_paper_id.grid(row=4, column=0)
        self.entry_paper_id.grid(row=4, column=1)
        self.check_classification_button.grid(row=5, column=0, columnspan=2)
        self.label_classification.grid(row=6, column=0, columnspan=2)

    def check_citation(self):
        paper_a_id = self.entry_paper_a_id.get()
        paper_b_id = self.entry_paper_b_id.get()
        with self.driver.session() as session:
            # result = session.read_transaction(self._find_citation_path, paper_a_id, paper_b_id)
            # result = session.execute_read_transaction(self._find_citation_path, paper_a_id, paper_b_id)
            result = session.read_transaction(self._find_citation_path, paper_a_id, paper_b_id)

            message = "Yes, through direct or indirect citations." if result else "No direct or indirect citations found."
            self.label_result.config(text=message)

    # def _find_citation_path(self, tx, paper_a_id, paper_b_id):
    #     query = """
    #     MATCH path = (a:Paper {id: $paper_a_id})-[:CITES*]->(b:Paper {id: $paper_b_id})
    #     RETURN path IS NOT NULL AS result
    #     """
    #     result = tx.run(query, paper_a_id=paper_a_id, paper_b_id=paper_b_id).single()[0]
    #     return result
    def _find_citation_path(self, tx, paper_a_id, paper_b_id):
          query = """
          MATCH path = (a:Paper {id: $paper_a_id})-[:CITES*]->(b:Paper {id: $paper_b_id})
          RETURN path IS NOT NULL AS result
          """
          result = tx.run(query, paper_a_id=paper_a_id, paper_b_id=paper_b_id).single()
          return result is not None and result[0]

    def _get_classification(self, tx, paper_id):
        query = """
        MATCH (p:Paper {id: $paper_id})
        RETURN p.class AS classification
        """
        result = tx.run(query, paper_id=paper_id)
        record = result.single()
        return record["classification"] if record else None

    def check_classification(self):
        paper_id = self.entry_paper_id.get()
        with self.driver.session() as session:
            classification = session.read_transaction(self._get_classification, paper_id)
            print("Classification:", classification)  # Add this line for debugging
            if classification:
                self.label_classification.config(text=classification)
            else:
                self.label_classification.config(text="No classification found.")

    def close(self):
        self.driver.close()

# Run the application
root = tk.Tk()
app = ResearchPapersDB(root)
root.mainloop()
app.close()
