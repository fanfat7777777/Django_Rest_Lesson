//import logo from './logo.svg';
import './App.css';
import React from 'react';
import axios from 'axios';
import {/*HashRouter,*/ BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom';
import Cookies from 'universal-cookie/lib';
import AuthorList from './components/Author';
import BookList from './components/Book';
import NotFound404 from './components/NotFound404';
import BookListAuthor from './components/BooksAuthor';
import LoginForm from './components/LoginForm';
import BookForm from './components/BookForm';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authorsProps':[],
      'booksProps':[],
      'token':'',
    }
  }


  createBook(name, author){
    const headers = this.get_headers()
    const data = {name:name, author:author}
    //console.log(name, author)
    axios.post('http://localhost:8000/api/books_router/', data, {headers}).then(
      response => {
        this.load_data()
      }
    ).catch(error => {
      console.log(error)
      this.setState({booksProps:[]})
    })
  }


  deleteBook(id){
    const headers = this.get_headers()
    console.log(headers)
    axios.delete(`http://localhost:8000/api/books_router/${id}`,{headers}).then(
      response => {
        //this.setState(
        //  {
        //    'booksProps':this.state.booksProps.filter((item) => item.id !== id)
        // }
        //)
        this.load_data()
      }
    ).catch(error => {
      console.log(error)
      this.setState({booksProps:[]})
    })
  }


  set_token(token) {
    console.log(token)
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token':token}, () => this.load_data())
  }


  is_auth() {
    return !!this.state.token
  }


  logout() {
    this.set_token('')
    this.setState({'authorsProps':[], 'booksProps':[]})
  }


  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token':token}, () => this.load_data())
  }


  get_token(username, password) {
    const data = {
      username:username, 
      password:password
    }

    axios.post('http://localhost:8000/api-token-auth/',data).then(
      response => {
        this.set_token(response.data['token'])
      }
    ).catch(error => console.log(error))
  }


  load_data() {
    const headers = this.get_headers()
    axios.get('http://localhost:8000/api/authors_router/',{headers}).then(
      response => {
        const authorsMount = response.data
        this.setState(
          {
            'authorsProps':authorsMount
          }
        )
      }
    ).catch(error => {
      console.log(error)
      //this.setState({authorsProps:[]})
    })

    //Книжки
    axios.get('http://localhost:8000/api/books_router/',{headers}).then(
      response => {
        const booksMount = response.data
        this.setState(
          {
            'booksProps':booksMount
          }
        )
      }
    ).catch(error => {
      console.log(error)
      //this.setState({booksProps:[]})
    })
  }


  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
    if (this.is_auth()) {
      headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
  }


  componentDidMount() {
    this.get_token_from_storage()
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
              <li>
                {
                  this.is_auth() ? 
                  <button onClick={() => this.logout()}>Logout</button> : 
                  <Link to='/login'>Login</Link>
                }
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <AuthorList authors={this.state.authorsProps} />} />

            <Route exact path='/books_router' component={() => 
              <BookList 
                books={this.state.booksProps} 
                deleteBook={(id) => this.deleteBook(id)} 
              />
            } />

            <Route exact path='/books_router/create' component={() => 
              <BookForm authors={this.state.authorsProps} createBook={(name, author) => this.createBook(name, author)} />} />

            <Route exact path='/login' component={() => <LoginForm 
              get_token={(username,password) =>this.get_token(username,password)} />} />

            <Route path='/author/:id'>
              <BookListAuthor books={this.state.booksProps}/>
            </Route>


            <Redirect from='/authors' to='/' />
            <Route component={NotFound404} />
          </Switch>
        </BrowserRouter>

      </div>
    )
  }
}



export default App;
