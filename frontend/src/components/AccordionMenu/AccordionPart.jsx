import React, { useState } from "react";
import CopyBox from "../CopyBox/CopyBox";
import "./AccordionPart.css"

const AccordionPart = ({ link }) => {

    const [isOpen, setIsOpen] = useState(false);

    function handleClick() {
        setIsOpen(!isOpen);
    }

    return (
        <div className="wrapper">
            <div className={`title-${isOpen ? 'open' : 'close'}`} onClick={handleClick}>
                <span>{link.alias}</span>
                <span><i className={`fa-solid fa-angle-${isOpen ? 'up' : 'down'}`}></i></span>
            </div>
            <div className={`info-${isOpen ? 'open' : 'close'}`}>
                <div className="urls"><CopyBox label={"Long URL:"} link={link.url}/><CopyBox label={"Short URL:"} link={"localhost:3000/" + link.alias}/></div>
            </div>
        </div>
    );
}

export default AccordionPart;