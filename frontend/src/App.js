import React, { useState, useEffect } from "react";
import axios from 'axios';
import AccordionMenu from "./components/AccordionMenu/AccordionMenu.jsx";
import Form from "./components/Form/Form.jsx";
import "./App.css";

export default function App() {

    const [urls, setUrls] = useState([]);

    const fetchUrls = () => {
        axios.get("http://localhost:8080/list_all", {withCredentials: true})
            .then((response) => {
                setUrls(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
    };

    useEffect(() => {
        fetchUrls();
    }, []);

    return (
        <div className="home-container">
            <nav className="navbar">
                <div className="logo"><h1>Shorter</h1></div>
                <div></div>
            </nav>
            <div className="middle-container">
                <div className="left-container">
                    <h1>SHORTEN YOUR <span>URL</span></h1>
                    <h4>Shorter allows you to shrink long url links for you to use and share!</h4>
                    {(urls.length > 0) && <Form handleFormSubmit={fetchUrls}/>}
                </div>
                <div className="right-container">
                    {(urls.length === 0) && <Form handleFormSubmit={fetchUrls}/>}
                    {(urls.length > 0) && <AccordionMenu links={urls}/>}
                </div>
            </div>
        </div>
    );

};