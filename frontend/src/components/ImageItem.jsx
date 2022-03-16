import React from 'react';
import {CardMedia, Paper} from "@material-ui/core";

const ImageItem = (props) => {
    const {image} = props;

    return (
        <Paper>
            <CardMedia
                image={image.url}
                sx={{maxHeight: 420, minHeight: 350}}
            />
        </Paper>
    );
};

export default ImageItem;