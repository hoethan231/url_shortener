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
                <div>
                    <h1>Right Side</h1>
                </div>
                <div>
                    <h1>Hello from the left side</h1>
                </div>
            </div>
        </div>
    );

};