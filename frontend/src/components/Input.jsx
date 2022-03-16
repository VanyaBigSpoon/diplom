import React, {forwardRef} from 'react';
import {TextField} from "@material-ui/core";

const Input = forwardRef((props, ref) => {
    return (
        <TextField
            variant="outlined"
            margin="normal"
            inputRef={ref}
            sx={{m: 1, width: '45ch'}}
            {...props}
        />
    )
})

export default Input;