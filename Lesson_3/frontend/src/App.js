//import logo from './logo.svg';
import './App.css';
import React from 'react';
import axios from 'axios';
import {HashRouter, BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom';
import AuthorList from './components/Author';
import BookList from './components/Book';
import NotFound404 from './components/NotFound404';
import BookListAuthor from './components/BooksAuthor';
//import UserList from './components/User'


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authorsProps':[],
      'booksProps':[],
      //'usersProps':[]
    }
  }

  componentDidMount() {
    
    axios.get('http://localhost:8000/api/authors_router/').then(
      response => {
        const authorsMount = response.data
        this.setState(
          {
            'authorsProps':authorsMount
          }
        )
      }
    ).catch(error => console.log(error))

    //Книжки
    axios.get('http://localhost:8000/api/books_router/').then(
      response => {
        const booksMount = response.data
        this.setState(
          {
            'booksProps':booksMount
          }
        )
      }
    ).catch(error => console.log(error))

    /*Юзеры
    axios.get('http://localhost:8000/api/users_router/').then(
      response => {
        const usersMount = response.data
        this.setState(
          {
            'usersProps':usersMount
          }
        )
      }
    ).catch(error => console.log(error))*/
    /*const authorsMount = [
      {
        'first_name':'Алек',
        'last_name':'Пуш',
        'birthday_year': 992,
      },
      {
        'first_name':'Александр',
        'last_name':'Шушк',
        'birthday_year':1975,
      }
    ]
    this.setState(
      {
        'authorsProps':authorsMount
      }
    )*/
  }


  render() {
    return (
      <div>
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/'>Authors</Link>
              </li>
              <li>
                <Link to='/books_router'>Books</Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <AuthorList authors={this.state.authorsProps} />} />
            <Route exact path='/books_router' component={() => <BookList books={this.state.booksProps} />} />
            
            <Route path='/author/:id'>
              <BookListAuthor books={this.state.booksProps}/>
            </Route>


            <Redirect from='/authors' to='/' />
            <Route component={NotFound404} />
          </Switch>
        </BrowserRouter>
        {/*Авторы
        <AuthorList authors={this.state.authorsProps} />
        <br/>
        Юзеры
        <UserList users={this.state.usersProps} />*/}
      </div>
    )
  }
}

/*function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload. УРААА
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}*/

export default App;
