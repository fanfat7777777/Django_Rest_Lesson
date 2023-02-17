import React from "react";
import {Link} from 'react-router-dom';

const AuthorItem = ({author}) => {
    return (
        <tbody>
            <tr>
                <td>
                    <Link to={`author/${author.id}`}>{author.first_name}</Link>
                </td>
                <td>
                    {author.last_name}
                </td>
                <td>
                    {author.birthday_year}
                </td>
            </tr>
        </tbody>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <thead>
                <tr>
                    <td>First Name</td>
                    <td>Last Name</td>
                    <td>Birthday year</td>
                </tr>
            </thead>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}

export default AuthorList;