from .models import Book
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def list_books(*_):
    return [
        {"id": book.id, "title": book.title, "description": book.desc}
        for book in Book.objects.all()
    ]

@convert_kwargs_to_snake_case
def create_book(*_, title : str, description: str):
    book = Book.objects.create(title=title, desc=description)
    return {"id": book.id, "title": book.title,"description": book.desc}


@convert_kwargs_to_snake_case
def update_book(*_, id : int, title : str, description: str):
    
    book = Book.objects.get(id=id)
    book.title = title
    book.desc = description
    book.save()
    return {"title": book.title,"description": book.desc}

@convert_kwargs_to_snake_case
def delete_book(*_, id : int):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return {"message": "Book deleted"}
    except Book.DoesNotExist:
        return {"message": "Book does not exist"}

@convert_kwargs_to_snake_case
def subscribe_to_books(*_):
    return [
        {"id": book.id, "title": book.title, "description": book.desc}
        for book in Book.objects.all()
    ]