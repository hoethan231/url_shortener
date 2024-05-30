import React from "react";
import Searchbar from "../Searchbar/Searchbar.jsx";
import "./Form.css";

const Form = ({onSearch}) => {

    return (
        <form className="form-wrapper">
            <div className="form-header"><h2>Create Link</h2></div>
            <div className="form-body">
                <label>Alias Here:</label>
                <Searchbar onSearch={onSearch}/>
                <label>Long URL Here:</label>
                <Searchbar onSearch={onSearch}/>
                <h7 className="error-message">That alias has already been used by this particular site :(</h7>
                <button type="submit">Create!</button>
            </div>
        </form>
    );

};

export default Form;