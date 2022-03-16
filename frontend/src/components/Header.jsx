import React, {useContext} from 'react';
import {AppBar, IconButton, Toolbar, Typography} from "@material-ui/core";
import {ExitToApp, HomeOutlined, HowToRegTwoTone, InputRounded, Person, ShoppingBasket} from "@material-ui/icons";
import {Link} from 'react-router-dom'
import {UserContext} from "../context/UserContext";


const Header = (props) => {
    const {handleBasket} = props;
    const [token, setToken] = useContext(UserContext);
    const handleLogout = () => {
        setToken(null);
    }

    return (
        <AppBar>
            <Toolbar>
                <Typography
                    variant="h6"
                    component="span"
                    sx={{flexGrow: 1}}
                >
                    Web-Shop
                </Typography>

                <Link to="/">
                    <IconButton
                        sx={{color: 'white'}}
                    >
                        <HomeOutlined/>
                    </IconButton>
                </Link>
                {token ? (
                    <>
                        <Link to="/user">
                            <IconButton
                                sx={{color: 'white'}}
                            >
                                <Person/>
                            </IconButton>
                        </Link>
                        <IconButton
                            sx={{color: 'white'}}
                            onClick={handleBasket}
                        >
                            <ShoppingBasket/>
                        </IconButton>
                        <IconButton sx={{color: 'white'}} onClick={handleLogout}>
                            <ExitToApp/>
                        </IconButton>
                    </>
                ) : (
                    <>
                        <Link to="/login">
                            <IconButton
                                sx={{color: 'white'}}
                            >
                                <InputRounded/>
                            </IconButton>
                        </Link>
                        <Link to="/registration">
                            <IconButton
                                sx={{color: 'white'}}
                            >
                                <HowToRegTwoTone/>
                            </IconButton>
                        </Link>
                    </>)}
            </Toolbar>
        </AppBar>
    )
        ;
};

export default Header;