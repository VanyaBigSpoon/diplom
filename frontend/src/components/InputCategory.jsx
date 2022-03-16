import React, {forwardRef, useState} from 'react';
import {MenuItem, TextField} from "@material-ui/core";

const currencies = [
    {
        value: 'Кроссовки',
    },
    {
        value: 'Туфли',
    },
    {
        value: 'Ботинки',
    },
    {
        value: 'Сандалии',
    },
];

const InputCategory = forwardRef((props, ref) => {
    return (
        <TextField

            select
            variant="outlined"
            margin="normal"
            inputRef={ref}
            sx={{m: 1, width: '45ch'}}
            {...props}
        >
            {currencies.map((option) => (
                <MenuItem key={option.value} value={option.value}>
                    {option.value}
                </MenuItem>
            ))}
        </TextField>
    )
})

export default InputCategory;