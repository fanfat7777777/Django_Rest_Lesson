import React from 'react';

class BookForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name:'',
            author:[],
        }
    }


    handleChange(event) {
        this.setState(
            {
                [event.target.name] : event.target.value
            }
        )
    }


    handleAuthorChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'author':[]
            })
            return;
        }
        let authors = []
        for (let i=0; i<event.target.selectedOptions.length; i++) {
            authors.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'author':authors
        })
    }


    handleSubmit(event) {
        console.log(this.state.name + ' ' + this.state.author)
        this.props.createBook(this.state.name, this.state.author)
        //this.props.get_token(this.state.login, this.state.password)

        event.preventDefault()
    }


    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                
                <div className='form-group'>
                    <label htmlFor='name'>name</label>
                    <input 
                        type='text' 
                        className='form-control' 
                        name='name' 
                        value={this.state.name}
                        onChange={(event) => this.handleChange(event)}
                    />
                </div>

                <div className='form-group'>
                <label htmlFor='author'>author</label>
                    {/*<select 
                        className='form-control' 
                        name='author' 
                        onChange={(event) => this.handleAuthorChange(event)}
                    >
                        {this.props.authors.map((item) =>
                            <option value={item.id}>
                                {item.first_name + ' ' + item.last_name}
                            </option>
                        )
                        }
                    </select>*/}
                    <select name='author' multiple onChange={(event) => this.handleAuthorChange(event)}>
                        {
                            this.props.authors.map((item) => 
                                <option value={item.id}>
                                    {item.first_name + ' ' + item.last_name}
                                </option>
                            )
                        }
                    </select>
                </div>

                <input type='submit' value='Save' />
            </form>

        )
    }
}

export default BookForm;