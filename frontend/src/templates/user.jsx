import React, {useContext, useEffect, useState} from 'react';
import {UserContext} from "../context/UserContext";
import Loader from "../components/Loader";
import {Button, Grid, Typography} from "@material-ui/core";
import {useForm} from "react-hook-form";
import InputUpdate from "../components/InputUpdate";
import Form from "../components/Form";


const User = () => {
    const [token] = useContext(UserContext)
    const [user, setUser] = useState();

    const getUser = async () => {
        const requestOption = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + token,
            },
        };
        const response = await fetch('/api/current_user/me', requestOption);
        const data = await response.json()
        if (response.ok) {
            setUser(data);
        }
    }

    const onSubmit = async (data) => {
        console.log(data);
        const requestOption = {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + token,
            },
            body: JSON.stringify({
                email: data.email,
                name: data.name,
                surname: data.surname,
                phone: data.phone,
            })
        };
        const response = await fetch('/api/user/me', requestOption);
        const dataResponse = await response.json()
        if (response.ok) {
            setUser(dataResponse);
        }
    }

    const {handleSubmit, register} = useForm({
        mode: "onBlur",
    })

    useEffect(() => {
        getUser();
    }, []);

    return (
        <>
            {
                user ? (
                    <Form onSubmit={handleSubmit(onSubmit)}>
                        <Grid container spacing={2}>
                            <Grid item xs={12} md={12}>
                                <Typography
                                    variant="h4"
                                    component="span"
                                >
                                    Здравствуйте {user.name}
                                </Typography>
                            </Grid>
                            <Grid item xs={12} md={12}>
                                <Typography
                                    variant="h6"
                                    component="span"
                                >
                                    Мои данные
                                </Typography>
                            </Grid>
                            <Grid item sx={12} md={4}>
                                <InputUpdate
                                    {...register('name')}
                                    type="text"
                                    label={user.name}
                                    name="name"
                                    helperText="Имя"
                                />
                            </Grid>
                            <Grid item sx={12} md={4}>
                                <InputUpdate
                                    {...register('surname')}
                                    type="text"
                                    label={user.surname}
                                    name="surname"
                                    helperText="Фамилия"
                                />
                            </Grid>
                            <Grid item sx={12} md={4}>
                                <InputUpdate
                                    {...register('phone')}
                                    type="text"
                                    label={user.phone}
                                    name="phone"
                                    helperText="Телефон"
                                />
                            </Grid>
                            <Grid item sx={12} md={4}>
                                <InputUpdate
                                    {...register('email')}
                                    type="text"
                                    label={user.email}
                                    name="email"
                                    helperText="Email"
                                />
                            </Grid>
                            <Grid item sx={12} md={4}>
                            </Grid>
                            <Grid item sx={12} md={4}>
                            </Grid>
                            <Grid item sx={12} md={4}>
                                <Button type="submit" size="large" variant="outlined">
                                    Сохранить
                                </Button>
                            </Grid>
                        </Grid>
                    </Form>
                ) : (
                    <Loader/>
                )
            }
        </>
    );
};

export default User;