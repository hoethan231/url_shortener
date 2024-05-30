import React from "react";
import Searchbar from "../Searchbar/Searchbar.jsx";
import "./Form.css";

const Form = ({onSearch}) => {

    return (
        <form className="form-wrapper">
            <div className="form-header"><h2>Create Link</h2></div>
            <div className="form-body">
                <label>Enter Long URL Here:</label>
                <Searchbar onSearch={onSearch}/>
                <button type="submit">Create!</button>
            </div>
        </form>
    );

};

export default Form;