import React, {useContext} from 'react';
import {Button, Grid, Typography} from "@material-ui/core";
import Form from "../components/Form";
import Input from "../components/Input";
import {useForm} from "react-hook-form";
import {UserContext} from "../context/UserContext";

const Registration = () => {
    const [, setToken] = useContext(UserContext)
    const {register, handleSubmit} = useForm({
        mode: "onBlur"
    })

    const onSubmit = async (data) => {
        console.log(data);
        if (data.password === data.passwordRepeat && data.password.length > 1) {
            console.log(data);
            const requestOptions = {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    email: data.email,
                    password: data.password,
                    name: data.name,
                    surname: data.surname,
                    phone: data.phone,
                })
            };
            const response = await fetch('/api/auth/registration', requestOptions);
            const answer = await response.json();
            if (response.ok) {
                setToken(answer.access_token);
            }
        }
    }

    return (
        <Form onSubmit={handleSubmit(onSubmit)}>
            <Grid
                container
                direction="column"
                justifyContent="center"
                alignItems="center"
                sx={{mt: '2rem'}}
            >
                <Typography component="h2" variant="h5" sx={{mt: '4rem'}}>Регистрация</Typography>
                <Input
                    {...register('name')}
                    id="name"
                    type="text"
                    label="Имя"
                    name="name"
                />
                <Input
                    {...register('surname')}
                    id="surname"
                    type="text"
                    label="Фамилия"
                    name="surname"
                />
                <Input
                    {...register('email')}
                    id="email"
                    type="text"
                    label="Email"
                    name="email"
                />
                <Input
                    {...register('phone')}
                    id="phone"
                    type="text"
                    label="Телефон"
                    name="phone"
                />
                <Input
                    {...register('password')}
                    id="password"
                    type="password"
                    label="Пароль"
                    name="password"
                />
                <Input
                    {...register('passwordRepeat')}
                    id="passwordRepeat"
                    type="password"
                    label="Повторите пароль"
                    name="passwordRepeat"
                />
                <Button type="submit" size="large" variant="outlined"
                        sx={{m: 1, width: '45ch'}}>Зарегистрироваться</Button>
            </Grid>
        </Form>
    );
};

export default Registration;