import { useParams } from "react-router-dom";


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


const BookListAuthor=({books}) => {
    let {id} = useParams();
    let filtered_items = books.filter((book => book.author.includes(parseInt(id))))

    return (
        <table>
            <thead>
                <tr>
                    <td>ID</td>
                    <td>Name</td>
                    <td>Author</td>
                </tr>
            </thead>
            {filtered_items.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default BookListAuthor;