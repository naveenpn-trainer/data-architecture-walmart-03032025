from google.cloud import  firestore

class CRUDOperations:
    def __init__(self):
        self.db = firestore.Client()

    ''''
    Add a document with auto generated id
    '''
    def add_document(self, collection_name, document):
        self.db.collection(collection_name).add(document)
    ''''
    Add document with custom document id
    '''
    def add_document_with_custom_id(self, document_id, collection_name , document):
        self.db.collection(collection_name).document(document_id).set(document)

    ''''
    Read document by document_id
    '''
    def read_document_by_document_id(self, collection_name, document_id):
        document_ref = self.db.collection(collection_name).document(document_id).get()
        if document_ref.exists:
            print(document_ref.to_dict())
        else:
            print("Document not found")

if __name__ == '__main__':
    crud_operations = CRUDOperations();
    collection_name = "users"
    document = {"name": "arjuna", "email": "arjuna.pn@gmail.com", "age": 26}
    # crud_operations.add_document(collection_name, document)

    # crud_operations.add_document_with_custom_id("1001", collection_name, document)
    crud_operations.read_document_by_document_id(collection_name,"1001")


