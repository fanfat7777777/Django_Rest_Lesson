//import logo from './logo.svg';
import './App.css';
import React from 'react';
import axios from 'axios';
import AuthorList from './components/Author';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authorsProps':[]
    }
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/app_authors/').then(
      response => {
        const authorsMount = response.data
        this.setState(
          {
            'authorsProps':authorsMount
          }
        )
      }
    ).catch(error => console.log(error))
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
        <AuthorList authors={this.state.authorsProps} />
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
