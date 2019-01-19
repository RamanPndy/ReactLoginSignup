import React, {Component} from 'react';
import MaterialUIForm from 'material-ui-form';
import { TextField, Button, Card, Typography, CardContent } from "@material-ui/core";

class Register extends Component {
    constructor (props) {
        super (props)
        this.state = {
            username:"",
            email:"",
            password:""
        }
    }

    handleSubmit = event => {
        let state_data = this.state
        let req_data = JSON.stringify(this.state) 
        console.log(state_data)
        console.log(req_data)
        let url = "http://127.0.0.1:8080/user/register"
        var data = new FormData();
        data.append( "json", state_data );

        fetch(url, {
            method: 'POST',
            mode : 'cors',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: req_data
            }).then(res=>res.json())
            .then(res => console.log(res));
    }

    handleOnChange = (event) => {
        event.preventDefault();
        const {name, value} = event.target
        switch (name){
            case "username":
                this.setState({username:value})
                break
            case "email":
                this.setState({email:value})
                break
            case "password":
                this.setState({password:value})
                break
            default:
                this.setState({username:"",email:"",password:""})
        }
    }

    render() {
        return ( 
            <Card className="register-card">
                <CardContent>
                    <Typography component="h2">
                        Create An Account
                    </Typography>
                    <MaterialUIForm onSubmit = {this.handleSubmit}>
                        <TextField 
                            label="username" 
                            type = "text"
                            name = "username"
                            data-validators ="isRequired,isAlpha"
                            onChange = {this.handleOnChange} />
                        <TextField 
                            label="email" 
                            type = "email"
                            name = "email"
                            onChange = {this.handleOnChange} />
                        <TextField 
                            label="password" 
                            type = "password"
                            name = "password"
                            onChange = {this.handleOnChange} />
                        <Button type = "submit">submit</Button>
                    </MaterialUIForm>
                </CardContent>
            </Card>
        )
    }
}

export default Register;