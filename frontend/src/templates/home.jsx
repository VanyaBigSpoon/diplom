import React, {useEffect, useState} from 'react';
import ProductsList from "../components/ProductList";
import SearchField from "../components/SearchField";
import Loader from "../components/Loader";
import {Grid, Pagination, PaginationItem} from "@material-ui/core";
import {NavLink} from "react-router-dom";
import CategoryMenu from "../components/CategoryMenu";

const Home = () => {
    const [products, setProducts] = useState();
    const [query, setQuery] = useState("");
    const [category, setCategory] = useState("");
    const [page, setPage] = useState(parseInt(products?.page || 1));
    const [value, setValue] = useState(0);

    const getProducts = async () => {
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch('/api/products' + '?page=' + (page - 1) + "&limit=9" + "&category=" + category + "&search=" +
                query, requestOptions
            )
        ;
        const data = await response.json();
        console.log(data);
        if (response.ok) {
            setProducts(data.products);
            setValue(data.value);
        }
    }

    useEffect(() => {
        getProducts();
    }, [query, page, category]);

    return (
        <>
            <CategoryMenu f={setCategory}/>
            <SearchField value={query} f={setQuery}/>
            {products ? (
                <>
                    <ProductsList products={products}/>
                    <Grid
                        container
                        direction="column"
                        justifyContent="center"
                        alignItems="center"
                        sx={{mt: '2rem', mb: '2rem'}}
                    >
                        <Pagination
                            count={value}
                            page={page}
                            onChange={(_, num) => setPage(num)}
                            showFirstButton
                            showLastButton
                            renderItem={(item) => (
                                <PaginationItem
                                    component={NavLink}
                                    to={`?page=${item.page}`}
                                    {...item}
                                />
                            )}
                        />
                    </Grid>
                </>
            ) : (<Loader/>)}

        </>
    );
};

export default Home;