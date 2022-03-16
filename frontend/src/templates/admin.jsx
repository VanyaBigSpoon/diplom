import React, {useContext, useEffect, useState} from 'react';
import {UserContext} from "../context/UserContext";
import {Button, Grid, Typography} from "@material-ui/core";
import Input from "../components/Input";
import FileUpload from 'react-material-file-upload';
import Form from "../components/Form";
import {useForm} from "react-hook-form";
import InputCategory from "../components/InputCategory";

const Admin = () => {
    const [admin, setAdmin] = useState();
    const [files, setFiles] = useState();

    const [currency, setCurrency] = useState();

    const change = (event) => {
        setCurrency(event.target.value);
    };

    const {handleSubmit, register} = useForm({
        mode: "onBlur",
    })
    const [token] = useContext(UserContext);

    const getAdmin = async () => {
        const requestOption = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + token,
            },
        };
        const response = await fetch("/api/admin/product", requestOption);
        const data = await response.json();
        if (response.ok) {
            setAdmin(data);
        }
    }

    const addSubmit = async (data) => {
        let formData = new FormData();
        if (files){
            files.forEach((file)=>{
                formData.append("files", file, file.name);
            });
        }
        const sizes = data.size.split(' ');
        sizes.forEach((s)=>{
            formData.append("size", s);
        });
        const str = '?name='+data.name+'&description='+data.description+'&price='+data.price+'&category='+data.category;
        console.log(formData);
        const requestOption = {
            method: "POST",
            headers: {
                Authorization: "Bearer "+token,
            },
            body: formData,
        }
        const response = await fetch("/api/admin/product"+str, requestOption);
        console.log(response);
    }

    useEffect(() => {
        getAdmin();
    }, []);

    return (
        <>
            {
                !admin ? (<></>) :
                    (<>
                        <Form onSubmit={handleSubmit(addSubmit)}>
                            <Grid
                                container
                                direction="column"
                                justifyContent="center"
                                alignItems="center"
                            >
                                <Typography component="h2" variant="h5" sx={{mt: '4rem'}}>Добавление продукта</Typography>
                                <Input
                                    {...register('name')}
                                    id="name"
                                    type="text"
                                    label="Название продукта"
                                    name="name"
                                />
                                <Input
                                    {...register('description')}
                                    id="description"
                                    type="textarea"
                                    label="Описание"
                                    name="description"
                                />
                                <Input
                                    {...register('price')}
                                    id="price"
                                    type="text"
                                    label="Цена"
                                    name="price"
                                />
                                <Input
                                    {...register('size')}
                                    id="size"
                                    type="text"
                                    label="Размер"
                                    name="size"
                                    helperText="Введите через пробел"
                                />
                                <InputCategory
                                    {...register('category')}
                                    id="filled-select-currency"
                                    type="text"
                                    label="Категория"
                                    name="category"
                                    helperText="Выберите категорию"
                                    currency={currency}
                                    handleChange={change}
                                />
                                <FileUpload value={files} onChange={setFiles}/>
                                <Button type="submit" size="large" variant="outlined"
                                        sx={{m: 1, width: '45ch'}}>Добавить
                                </Button>
                            </Grid>
                        </Form>
                    </>)
            }
        </>
    );
};

export default Admin;