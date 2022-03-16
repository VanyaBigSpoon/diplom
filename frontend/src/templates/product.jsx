import React, {useContext, useEffect, useState} from 'react';
import {useParams} from "react-router-dom";
import {Button, Grid, Typography} from "@material-ui/core";
import Carousel from 'react-material-ui-carousel';
import ImageItem from "../components/ImageItem";
import Loader from "../components/Loader";
import {UserContext} from "../context/UserContext";


const Product = () => {
    const {id} = useParams();
    useEffect(() => {
        getProduct();
    }, []);

    const [element, setProduct] = useState();
    const [token] = useContext(UserContext);

    const addProductToBasket = async (id) => {
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + token,
            },
        };
        const response = await fetch('/api/products/'+id, requestOptions);
        if (response.ok){
            console.log("ok");
        }
    }

    const getProduct = async () => {
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch('/api/products/' + id, requestOptions);
        const data = await response.json();
        console.log(response)
        if (response.ok) {
            setProduct(data);
        }
    }

    return (
        <>
            {element ?
                (
                    <Grid container spacing={2}>
                        <Grid item xs={12} md={12}>
                            <Typography
                                variant="h4"
                                component="span"
                            >
                                {element.product.name}
                            </Typography>
                        </Grid>
                        <Grid item xs={12} md={8}>
                            <Carousel>
                                {
                                    element.images.map((image) => <ImageItem image={image}/>)
                                }
                            </Carousel>
                        </Grid>
                        <Grid item xs={12} md={4}>
                            <Typography
                                variant="h6"
                                component="p"
                            >
                                {element.product.description}
                            </Typography>
                        </Grid>
                        <Grid item xs={4} md={4}>
                            <Typography
                                variant="h6"
                                component="span"
                            >
                                Цена: {element.product.price} рублей.
                            </Typography>
                        </Grid>
                        <Grid item xs={4} md={4}>
                            <Button onClick={() => addProductToBasket(element.product.product_id)} variant="contained">
                                Добавить в корзину
                            </Button>
                        </Grid>

                    </Grid>
                )
                : (
                    <Loader />
                )
            }
        </>
    );
};

export default Product;