import React from "react";

const BookItem = ({book}) => {
    return (
        <tbody>
            <tr>
                <td>{book.id}</td>
                <td>{book.name}</td>
                <td>{book.author}</td>
            </tr>
        </tbody>
    )
}

const BookList = ({books}) => {
    return (
        <table>
            <thead>
                <tr>
                    <td>ID</td>
                    <td>Name</td>
                    <td>Author</td>
                </tr>
            </thead>
            {books.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default BookList;