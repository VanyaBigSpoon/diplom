import React, {forwardRef} from 'react';
import {TextField} from "@material-ui/core";

const InputUpdate = forwardRef((props, ref) => {
    return (
        <TextField
            variant="standard"
            margin="normal"
            inputRef={ref}
            {...props}
        />
    )
})

export default InputUpdate;