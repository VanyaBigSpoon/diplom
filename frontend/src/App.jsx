import {Route, Routes} from 'react-router-dom';
import Header from "./components/Header";
import Home from "./templates/home";
import NotFound from "./templates/notFound";
import User from "./templates/user";
import Registration from "./templates/registration";
import Login from "./templates/login";
import {Container} from "@material-ui/core";
import React, {useState} from "react";
import {UserProvider} from "./context/UserContext";
import Admin from "./templates/admin";
import Product from "./templates/product";
import Basket from "./components/Basket";


function App() {
    const [isBasketOpen, setBasketOpen] = useState(false);

    return (
        <UserProvider>
            <Header handleBasket={() => setBasketOpen(true)}/>
            <Container
                sx={{mt: '5rem'}}
            >
                <Routes>
                    <Route path="/registration" element={< Registration/>}/>
                    <Route path="/login" element={< Login/>}/>
                    <Route path="/" element={< Home/>}/>
                    <Route path="/user" element={< User/>}/>
                    <Route path="/admin" element={< Admin/>}/>
                    <Route path="/product/:id" element={< Product/>}/>
                    <Route path="*" element={< NotFound/>}/>
                </Routes>
            </Container>
            <Basket basketOpen={isBasketOpen} closeBasket={() => setBasketOpen(false)}/>
        </UserProvider>
    );
}

export default App;
