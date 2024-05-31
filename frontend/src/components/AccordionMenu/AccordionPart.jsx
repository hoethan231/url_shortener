import React, { useState } from "react";
import axios from "axios";
import CopyBox from "../CopyBox/CopyBox";
import "./AccordionPart.css"

const AccordionPart = ({ link, onUrlDelete }) => {

    const [isOpen, setIsOpen] = useState(false);

    function handleOpen() {
        setIsOpen(!isOpen);
    }

    const handleDelete = () => {
        axios.get(`http://localhost:8080/delete_url/${link.alias}`, { withCredentials: true })
        .then((response) => {
            console.log(response);
            onUrlDelete();
        })
        .catch((error) => {
            const errorMsg = error.response?.data?.message || error.message || "An error occurred";
            console.log(errorMsg);
        });
    };

    return (
        <div className="wrapper">
            <div className={`title-${isOpen ? 'open' : 'close'}`} onClick={handleOpen}>
                <span>{link.alias}</span>
                <div className="title-elements">
                    {isOpen && <span><i className="fa-solid fa-trash-can" onClick={handleDelete}></i></span>}
                    <span><i className={`fa-solid fa-angle-${isOpen ? 'up' : 'down'}`}></i></span>
                </div>
            </div>
            <div className={`info-${isOpen ? 'open' : 'close'}`}>
                <div className="urls"><CopyBox label={"Long URL:"} link={link.url}/><CopyBox label={"Short URL:"} link={"localhost:3000/" + link.alias}/></div>
            </div>
        </div>
    );
}

export default AccordionPart;