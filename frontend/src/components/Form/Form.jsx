import React, { useState } from "react";
import axios from "axios";
import "./Form.css";

const Form = ({ handleFormSubmit }) => {

    const [alias, setAlias] = useState("");
    const [url, setUrl] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        if(alias !== "" && url !== "")  {
            axios.post("http://localhost:8080/create_url", { alias: alias, url: url }, {withCredentials: true})
            .then((response) => {
                console.log(response);
                handleFormSubmit();
                setAlias("");
                setUrl("");
                setErrorMessage("");
            })
            .catch((error) => {
                const errorMsg = error.response?.data?.message || error.message || "An error occurred";
                setErrorMessage(errorMsg);
                console.log(error);
            });
        } else {
            setErrorMessage("Please fill out all fields!");
        }
    };

    return (
        <form className="form-wrapper" onSubmit={handleSubmit}>
            <div className="form-header"><h2>Create Link</h2></div>
            <div className="form-body">     
                <label>Alias Here:</label>
                <input type="text" value={alias} placeholder="Paste Here!" onChange={(e) => setAlias(e.target.value)}/>
                <label>Long URL Here:</label>
                <input type="text" value={url} placeholder="Paste Here!" onChange={(e) => setUrl(e.target.value)}/>
                <h3 className="error-message">{errorMessage}</h3>
                <button type="submit">Create!</button>
            </div>
        </form>
    );

};

export default Form;