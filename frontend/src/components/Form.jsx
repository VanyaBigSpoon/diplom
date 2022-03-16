import React from 'react';
import { makeStyles } from '@material-ui/styles';

const useStyles = makeStyles({
    root: {
        width: "100%",
    },
})


const Form = ({children, ...props}) => {
    const styles = useStyles();

    return (
        <form className={styles.root} noValidate {...props} method="POST">
            {children}
        </form>
    );
};

export default Form;