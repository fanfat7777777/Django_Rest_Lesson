import React from "react";
import { Link } from "react-router-dom";

const BookItem = ({book, deleteBook}) => {
    return (
        <tbody>
            <tr>
                <td>{book.id}</td>
                <td>{book.name}</td>
                <td>{book.author}</td>
                <td>
                    <button onClick={() => deleteBook(book.id)} type='button'>Delete</button>
                </td>
            </tr>
        </tbody>
    )
}

const BookList = ({books, deleteBook}) => {
    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <td>ID</td>
                        <td>Name</td>
                        <td>Author</td>
                        <td></td>
                    </tr>
                </thead>
                {books.map((book) => <BookItem book={book} deleteBook={deleteBook} />)}
            </table>
            <Link to='/books_router/create'>Create</Link>
        </div>
    )
}

export default BookList;