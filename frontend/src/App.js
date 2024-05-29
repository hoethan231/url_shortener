import React, { useState } from "react";
import Searchbar from "./components/Searchbar/Searchbar";
import "./App.css";

export default function App() {

    const [input, setInput] = useState("");

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
                    
                </div>
                <div className="right-container">

                </div>
            </div>
        </div>
    );

};