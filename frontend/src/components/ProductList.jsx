import React from 'react';
import {Grid} from "@material-ui/core";
import ProductItem from "./ProductItem";

const ProductsList = (props) => {
    const {products} = props;

    return (
        <Grid container spacing={2} sx={{pt: 2}}>
            {products?.map((item) => (
                <ProductItem key={item.Products.product_id}  {...item}/>
            ))}

        </Grid>
    );
};

export default ProductsList;