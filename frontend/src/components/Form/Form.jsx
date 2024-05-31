import React, { useState } from "react";
import axios from "axios";
import "./Form.css";

const Form = ({ handleFormSubmit }) => {

    const [alias, setAlias] = useState("");
    const [url, setUrl] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    const isValidUrl = (string) => {
        try {
            new URL(string);
            return true;
        } catch (error) {
            return false;
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (alias === "" || url === "") {
            setErrorMessage("Please fill out all fields!");
            return;
        }

        if (!isValidUrl(url)) {
            setErrorMessage("Please enter a valid URL!");
            return;
        }

        const invalidChars = "{}|\^[]`;/?:@&=+$,";
        for(let i=0; i<alias.length; i++) {
            if(invalidChars.includes(alias.charAt(i))) {
                setErrorMessage("Please do not use invalid or special characters in your alias");
                return;
            }
        }

        axios.post("http://localhost:8080/create_url", { alias: alias.replace(" ", "-"), url: url.replace(" ", "-") }, { withCredentials: true })
            .then((response) => {
                console.log(response);
                handleFormSubmit();
                setAlias("");
                setUrl("");
                setErrorMessage("");
            })
            .catch((error) => {
                const errorMsg = error.response?.data?.message || error.response.data.detail || error.message || "An error occurred";
                setErrorMessage(errorMsg);
                console.log(error);
            });
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