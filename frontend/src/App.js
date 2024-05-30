import React, { useState } from "react";
import AccordionMenu from "./components/AccordionMenu/AccordionMenu.jsx";
import Form from "./components/Form/Form.jsx";
import "./App.css";

export default function App() {

    const [input, setInput] = useState("");
    const [urls, setUrls] = useState([1]);

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
                    {(urls.length > 0) && <Form onSearch={setInput}/>}
                </div>
                <div className="right-container">
                    {(urls.length === 0) && <Form onSearch={setInput}/>}
                    {(urls.length > 0) && <AccordionMenu/>}
                </div>
            </div>
        </div>
    );

};