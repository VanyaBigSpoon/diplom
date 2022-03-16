import React from 'react';
import {Button, Grid} from "@material-ui/core";
import {Close} from "@material-ui/icons";

const CategoryMenu = (props) => {
    return (
        <Grid
            container
            direction="row"
            justifyContent="center"
            alignItems="center"
            sx={{mt: '2rem'}}
        >
            <Button variant="standard" onClick={()=>props.f("Кроссовки")}>Кроссовки</Button>
            <Button variant="standard" onClick={()=>props.f("Туфли")}>Туфли</Button>
            <Button variant="standard" onClick={()=>props.f("Ботинки")}>Ботинки</Button>
            <Button variant="standard" onClick={()=>props.f("Сандалии")}>Сандалии</Button>
            <Button variant="standard" onClick={()=>props.f("")}><Close/></Button>
        </Grid>
    );
};

export default CategoryMenu;