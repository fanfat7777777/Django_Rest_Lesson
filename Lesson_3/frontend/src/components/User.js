import React from "react";


const UserItem = ({user}) => {
    return (
        <tbody>
            <tr>
                <td>{user.username}</td>
                <td>{user.firstname}</td>
                <td>{user.last_name}</td>
                <td>{user.email}</td>
            </tr>
        </tbody>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <thead>
                <tr>
                    <td>User Name</td>
                    <td>First Name</td>
                    <td>Last Name</td>
                    <td>Email</td>
                </tr>
            </thead>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}

export default UserList;