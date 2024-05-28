import React, { useState } from "react";
import "./Searchbar.css";

const Searchbar = ({onSearch}) => {

    const [query, setQuery] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch(query);
    };

    return (
        <form className="input-wrapper" onClick={handleSubmit}>
            <input value={query} onChange={(e) => setQuery(e.target.value)}/>
        </form>
    );
};

export default Searchbar;