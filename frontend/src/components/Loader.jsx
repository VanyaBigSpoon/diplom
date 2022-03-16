import React from 'react';
import {Grid} from "@material-ui/core";
import {Oval} from "react-loader-spinner";

const Loader = () => {
    return (
        <Grid container spacing={2} justifyContent="center"
              alignItems="center" sx={{pt: 15}}>
            <Grid item xs={5} md={5}/>
            <Grid item xs={2} md={2}>
                <Oval
                    height="50"
                    width="50"
                    color='grey'
                    ariaLabel='loading'
                />
            </Grid>
            <Grid item xs={5} md={5}/>
        </Grid>
    );
};

export default Loader;