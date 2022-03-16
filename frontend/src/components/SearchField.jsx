import React from 'react';
import {Grid, TextField} from "@material-ui/core";

const SearchField = (props) => {
    return (
        <Grid container spacing={2}>
            <Grid item xs={12} md={12}>
                <TextField
                    fullWidth
                    label='Поиск'
                    type='search'
                    variant='standard'
                    value={props.value}
                    onChange={(event) => props.f(event.target.value)}
                />
            </Grid>
        </Grid>
    );
};

export default SearchField;