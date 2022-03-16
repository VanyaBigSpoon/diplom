import React, {useContext} from 'react';
import Form from "../components/Form";
import {Button, Grid, Typography} from "@material-ui/core";
import Input from "../components/Input";
import {useForm} from "react-hook-form";
import {UserContext} from "../context/UserContext";

const Login = () => {
    const [, setToken] = useContext(UserContext);

    const {register, handleSubmit} = useForm({
        mode: "onBlur"
    })

    const onSubmit = async (data) => {
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: JSON.stringify('grant_type=&username=' + data.username + '&password=' + data.password + '&scope=&client_id=&client_secret='),
            mode: 'no-cors',
        };
        const response = await fetch("/api/auth/token", requestOptions);
        const answer = await response.json();
        if (response.ok) {
            setToken(answer.access_token);
        }
    }

    return (
        <Form onSubmit={handleSubmit(onSubmit)}>
            <Grid
                container
                direction="column"
                justifyContent="center"
                alignItems="center"
            >
                <Typography component="h2" variant="h5" sx={{mt: '4rem'}}>Авторизация</Typography>
                <Input
                    {...register('username')}
                    id="username"
                    type="text"
                    label="Email"
                    name="username"
                />
                <Input
                    {...register('password')}
                    id="password"
                    type="password"
                    label="Пароль"
                    name="password"
                />
                <Button type="submit" size="large" variant="outlined" sx={{m: 1, width: '45ch'}}>Войти</Button>
            </Grid>
        </Form>
    );
};

export default Login;