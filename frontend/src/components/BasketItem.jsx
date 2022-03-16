import React from 'react';
import {ListItem, ListItemButton, ListItemText, Typography} from "@material-ui/core";
import {Close} from "@material-ui/icons";
import {Link} from "react-router-dom";

const BasketItem = (props) => {
    const {removeFromBasket, product_id, name, price} = props;
    return (
        <ListItem >
            <ListItemText>
                <Typography>
                    <Link to={"/product/"+product_id}>
                        {name}
                    </Link>
                     {" Цена: " + price + " руб."}
                </Typography>
            </ListItemText>
            <ListItemButton onClick={() => removeFromBasket(product_id)}>
                <Close />
            </ListItemButton>
        </ListItem>
    );
};

export default BasketItem;