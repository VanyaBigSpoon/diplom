import React, {useContext} from 'react';
import {Button, Card, CardActions, CardContent, CardMedia, Grid, Typography} from "@material-ui/core";
import {Link} from "react-router-dom";
import {useForm} from "react-hook-form";
import Form from "./Form";
import {UserContext} from "../context/UserContext";

const ProductItem = (props) => {

    const {register, handleSubmit} = useForm({
        mode: "onBlur"
    })
    const [token] = useContext(UserContext);

    const addProductToBasket = async (data) => {
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + token,
            },
        };
        const response = await fetch('/api/products/'+data.id, requestOptions);
        if (response.ok){
            console.log("ok");
        }
    }

    const {Products, url} = props;

    return (
        <Grid item xs={12} md={4}>
            <Card sx={{height: '100%'}}>
                <CardMedia
                    image={url}
                    alt={Products.name}
                    titile={Products.name}
                    sx={{height: 140}}
                />
                <CardContent>
                    <Typography
                        variant="h6"
                        component="h3"
                    >
                        {Products.name}
                    </Typography>
                    <Typography
                        variant="body1"
                    >Цена: {Products.price} руб.</Typography>
                </CardContent>
                <CardActions>
                    <Form onSubmit={handleSubmit(addProductToBasket)}>
                        <Button
                            variant="text"
                            type="submit"
                            {...register("id")}
                            name={Products.product_id}
                            value={Products.product_id}
                        >
                            Добавить в корзину
                        </Button>
                    </Form>
                </CardActions>
                <CardActions>
                    <Link to={"/product/" + Products.product_id}>
                        <Button
                            variant="text"
                        >
                            Открыть
                        </Button>
                    </Link>
                </CardActions>
            </Card>
        </Grid>
    );
};

export default ProductItem;