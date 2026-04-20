from app.db.models import ChatHistory, Document


def save_chat(db, query, response, context="", user_id=None):
    chat = ChatHistory(
        user_id=user_id,
        query=query,
        response=response,
        context=context
    )
    db.add(chat)
    db.commit()


def save_document(db, file_name):
    doc = Document(file_name=file_name)
    db.add(doc)
    db.commit()