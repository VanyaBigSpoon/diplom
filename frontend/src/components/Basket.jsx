import React, {useContext, useEffect, useState} from 'react';
import {Divider, Drawer, List, ListItem, ListItemButton, ListItemIcon, ListItemText} from "@material-ui/core";
import {ShoppingBasket} from "@material-ui/icons";
import BasketItem from "./BasketItem";
import {UserContext} from "../context/UserContext";

const Basket = (props) => {
    const {
        basketOpen,
        closeBasket = Function.prototype,
    } = props;

    const [order, setOrder] = useState();
    const [token] = useContext(UserContext);

    const getOrder = async () => {
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + token,
            },

        };
        const response = await fetch('/api/basket', requestOptions);
        const data = await response.json();
        console.log(data);
        if(response.ok){
            setOrder(data);
        }
    }

    useEffect(() => {
        getOrder();
    }, []);

    const removeFromBasket = async (id) => {
        const requestOptions = {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + token,
            },
        };
        const response = await fetch('/api/basket/'+id, requestOptions);
        if (response.ok){
            console.log("ok");
            await getOrder();
        }
    }

    return (
        <Drawer
            anchor="right"
            open={basketOpen}
            onClose={closeBasket}
        >
            <List sx={{width: '350px'}}>
                <ListItem>
                    <ListItemIcon>
                        <ShoppingBasket/>
                    </ListItemIcon>
                    <ListItemText primary="Корзина"/>
                </ListItem>
                <Divider/>
                {
                    !order?.length ? (
                        <ListItemText primary="Корзина пуста"/>
                    ) : (
                        order.map((item) => (
                            <BasketItem key={item} removeFromBasket={removeFromBasket} {...item}/>
                        ))
                    )
                }
                <Divider/>
                {
                    !order?.length ? (
                        ":("
                    ) : (
                        <ListItemButton>
                            Купить
                        </ListItemButton>
                    )
                }
            </List>
        </Drawer>
    );
};

export default Basket;